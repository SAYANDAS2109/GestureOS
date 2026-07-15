import cv2
import mediapipe as mp
import math



class HandTracker:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]

    def findHands(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        landmark_list = []

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

               self.mpDraw.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )
               h, w, c = frame.shape

               

                

               for idx, lm in enumerate(hand.landmark):

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    landmark_list.append([idx, cx, cy])

        return frame, landmark_list
    def fingersUP(self,landmark_list):
        fingers = []

        if not landmark_list:
            return fingers
        #THUMBB
        if landmark_list[self.tip_ids[0]][1] > landmark_list[self.tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #OTHER FINGERS NOW
        for i in range(1,5):
            if landmark_list[self.tip_ids[i]][2] < landmark_list[self.tip_ids[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
    

    def findDistance(self,p1,p2,landmark_list,frame):
        x1,y1 = landmark_list[p1][1], landmark_list[p1][2]
        x2, y2 = landmark_list[p2][1], landmark_list[p2][2]

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2


        length = math.hypot(x2 - x1,y2-y1)

        cv2.circle(frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(frame, (cx, cy), 8, (0, 255, 0), cv2.FILLED)
        print(f"Thumb: ({x1}, {y1})  Index: ({x2}, {y2})")
        return length , frame 
    
    

        
                        