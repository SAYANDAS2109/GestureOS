# ✋ GestureOS - Gesture Controlled Desktop Automation

> Control your computer using hand gestures powered by Computer Vision.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![License](https://img.shields.io/badge/License-MIT-red)

---

## 📌 Overview

GestureOS is a real-time hand gesture controlled desktop automation system built using **Python**, **OpenCV**, and **MediaPipe**.

The application tracks hand landmarks using a webcam and translates predefined gestures into desktop actions such as:

- 💡 Brightness Control
- 📸 Screenshot Capture
- 📜 Scrolling
- 🖱️ Virtual Mouse
- 🤏 Drag & Drop

The project demonstrates practical applications of computer vision and human-computer interaction (HCI) without requiring any specialized hardware.



---

## 📷 Screenshots

### Brightness Mode

(<img width="1916" height="1073" alt="Screenshot 2026-07-15 191539" src="https://github.com/user-attachments/assets/03228a76-b88a-4118-a63c-de0d48508de7" />
)

### Screenshot Mode

(<img width="1917" height="1075" alt="Screenshot 2026-07-15 191624" src="https://github.com/user-attachments/assets/d7ef72b5-eb9f-4c7a-8a54-4e431d94f41b" />
)

### Scroll Mode

(<img width="1917" height="1077" alt="Screenshot 2026-07-15 191608" src="https://github.com/user-attachments/assets/8ddc7c4d-0f61-4a0b-9107-9fb78c82a4d7" />
)

### Cursor Mode

(<img width="1917" height="1078" alt="Screenshot 2026-07-15 191637" src="https://github.com/user-attachments/assets/d5a2e9d4-8766-4bec-9bd9-df8fd4253b5c" />
)

---

# ✨ Features

- ✅ Real-time hand tracking
- ✅ 21 hand landmark detection
- ✅ Finger state recognition
- ✅ Gesture-based mode switching
- ✅ Brightness control using pinch distance
- ✅ Screenshot capture using gesture
- ✅ Gesture-based scrolling
- ✅ Virtual mouse cursor
- ✅ Drag & Drop support
- ✅ Smooth cursor movement
- ✅ Mode locking to prevent accidental switching

---

# 🖐️ Supported Gestures

| Gesture | Function |
|---------|----------|
| ☝️ Index Finger | Activate Brightness Mode |
| ✌️ Index + Middle | Activate Scroll Mode |
| 👍 Thumb | Activate Screenshot Mode |
| 🤙 Thumb + Pinky | Activate Cursor Mode |
| ✋ Open Palm | Return to Main Menu |
| ✊ Closed Fist | Capture Screenshot (inside Screenshot Mode) |

---

# 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- Screen Brightness Control

---

# 📂 Project Structure

```
GestureOS/
│
├── modules/
│   └── hand_tracker.py
├── app.py
├── requirements.txt

```

---

# ⚙️ Installation

Clone the repository

```bash
git clone (https://github.com/SAYANDAS2109/GestureOS)
```

Move into the project

```bash
cd GestureOS
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

# 🚀 How It Works

1. Webcam captures live video.
2. MediaPipe detects the hand and extracts 21 landmarks.
3. Finger states are determined using landmark positions.
4. A gesture recognition module identifies the active gesture.
5. GestureOS switches to the selected mode.
6. The corresponding desktop action is executed.

---

# 💡 Future Improvements

- Voice command integration
- Volume control
- Media player controls
- Presentation mode
- Gesture customization
- Multi-hand support
- AI-based gesture learning
- Cross-platform optimization

---

# 📈 Skills Demonstrated

- Computer Vision
- Human Computer Interaction (HCI)
- Real-Time Image Processing
- Gesture Recognition
- Desktop Automation
- Python Development
- State Machine Logic
- Event Handling

---

# 👨‍💻 Author

**Sayan Das**

Petroleum Engineering Undergraduate  
IIT (ISM) Dhanbad

GitHub: (https://github.com/SAYANDAS2109)

LinkedIn: inkedin.com/in/sayan-das-1466b1369/

---


