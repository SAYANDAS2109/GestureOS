import cv2
from modules.hand_tracker import HandTracker
import numpy as np
import screen_brightness_control as sbc
import pyautogui
import time


cap = cv2.VideoCapture(0)

tracker = HandTracker()
mode = "NONE"
gesture_start = None
pending_mode = None
gesture_locked = False
screenshot_start = None
screenshot_taken = False
prev_y = None
screen_width, screen_height = pyautogui.size()
prev_x = 0
prev_y_cursor = 0

smoothening = 12
dragging = False

while True:

    success, frame = cap.read()

    if not success:
        break

    frame,landmark_list = tracker.findHands(frame)
    fingers =[]
    desired_mode = None
    if landmark_list:
        fingers = tracker.fingersUP(landmark_list)

    if mode == "NONE":

        if fingers == [0, 1, 0, 0, 0]:
            desired_mode = "BRIGHTNESS"

        elif fingers == [0, 1, 1, 0, 0]:
            desired_mode = "SCROLL"

        elif fingers == [1, 0, 0, 0, 0]:
            desired_mode = "SCREENSHOT"
        elif fingers == [1,0,0,0,1]:
            desired_mode ="CURSOR"

    # Exit current mode
    if mode != "NONE" and fingers == [1, 1, 1, 1, 1]:

        mode = "NONE"

        gesture_locked = False
        pending_mode = None
        gesture_start = None

        screenshot_start = None
        screenshot_taken = False

        prev_y = None
        prev_x=0
        prev_y=0
        if dragging:
            pyautogui.mouseUp()
            dragging=False


        
        
    if desired_mode is not None and not gesture_locked:

        if pending_mode != desired_mode:
            pending_mode = desired_mode
            gesture_start = time.time()

        elif time.time() - gesture_start > 1:

            mode = pending_mode
            pending_mode = None
            gesture_start = None
            gesture_locked = True

    # Only reset while we are in the main menu
    if mode == "NONE" and desired_mode is None:
        gesture_locked = False
        pending_mode = None
        gesture_start = None





    
    if landmark_list:
        if mode == "BRIGHTNESS":
        # fingers = tracker.fingersUP(landmark_list)
            length,frame = tracker.findDistance(
            4,
            8,
            landmark_list,
            frame
        
        )
            brightness = np.interp(length, [30, 200], [0, 100])
            sbc.set_brightness(int(brightness))

            cv2.putText(
            frame,
            f'Brightness:{int(brightness)}%',
            (20,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )
        elif mode == "SCREENSHOT":
            if fingers == [0,0,0,0,0]:
                if screenshot_start is None:
                    screenshot_start=time.time()
                elapsed = time.time() - screenshot_start
                cv2.putText(
                    frame,
            f"Hold: {elapsed:.1f}s",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
                )
                if elapsed>=2 and not screenshot_taken:
                    filename = f"Screenshot_{int(time.time())}.png"
                    screenshot = pyautogui.screenshot()
                    screenshot.save(filename)
                    screenshot_taken=True

                    cv2.putText(
                    frame,
    "Screenshot Saved!",
    (20, 150),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
                )
            else:
                screenshot_start=None
                screenshot_taken=False
        elif mode == "SCROLL":
            if fingers == [0,1,0,0,0]:
                index_y = landmark_list[8][2]
                if prev_y is not None:
                    difference = index_y - prev_y
                    if abs(difference)>8:
                        scroll_amount = int(difference * 4)
                        pyautogui.scroll(-scroll_amount)
                prev_y=index_y
            else:
                prev_y = None


        
        
        
        elif mode == "CURSOR":
            print("Cursor mode running")
            if fingers == [0,1,0,0,0]:
                x = landmark_list[8][1]
                y= landmark_list[8][2]
                print(x,y)

                frame_h, frame_w,_ = frame.shape
                margin =100
                screen_x = np.interp(
                    x,
                    [margin,frame_w - margin],
                    [0,screen_width])
                
                screen_y = np.interp(
                    y,
                    [margin,frame_h - margin],
                    [0,screen_height]
                )

                curr_x = prev_x + (screen_x - prev_x) / smoothening
                curr_y = prev_y_cursor + (screen_y - prev_y_cursor) / smoothening
                pyautogui.moveTo(int(curr_x), int(curr_y))
                length,frame = tracker.findDistance(
                    4,8,
                    landmark_list,
                    frame
                )
                if length < 25 and not dragging:
                    pyautogui.mouseDown()
                    dragging=True
                elif length>45 and dragging:
                    pyautogui.mouseUp()
                    dragging = False
                status = "Dragging" if dragging else "Cursor"
                cv2.putText(
                    frame,
                    status,
                    (20, 170),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 255),
                    2
                )
                prev_x = curr_x
                prev_y_cursor=curr_y
            else:
                prev_x=0
                prev_y_cursor=0
    cv2.putText(
        frame,
    f"MODE : {mode}",
    (20, 90),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 0),
    2
    )   

    if pending_mode is not None and gesture_start is not None:
        remaining = max(0, 1 - (time.time() - gesture_start))
        cv2.putText(
            frame,
        f"Hold: {remaining:.1f}s",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
        )
    
    cv2.imshow("GestureOS", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    


cap.release()
cv2.destroyAllWindows()
