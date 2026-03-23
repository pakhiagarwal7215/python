import cv2
import mediapipe as mp
import numpy as np
from math import hypot
import screen_brightness_control as sbc

# ===================== PYCAW =====================
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# ===================== MEDIAPIPE =====================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ===================== VOLUME INIT =====================
try:
    speakers = AudioUtilities.GetSpeakers()
    interface = speakers._dev.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    min_vol, max_vol, _ = volume.GetVolumeRange()
    print("Volume control ready")
except Exception as e:
    print("Pycaw error:", e)
    exit()

# ===================== BRIGHTNESS INIT =====================
try:
    monitors = sbc.list_monitors()
    print("Detected monitors:", monitors)
    current_brightness = sbc.get_brightness(display=0, method='wmi')[0]
except Exception as e:
    print("Brightness not supported:", e)
    monitors = None

# ===================== CAMERA =====================
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

# ===================== MAIN LOOP =====================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    h, w, _ = frame.shape

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, handLms in enumerate(results.multi_hand_landmarks):

            label = results.multi_handedness[i].classification[0].label
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            thumb = handLms.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index = handLms.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            x1, y1 = int(thumb.x * w), int(thumb.y * h)
            x2, y2 = int(index.x * w), int(index.y * h)

            cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            distance = hypot(x2 - x1, y2 - y1)

            # ===================== RIGHT HAND → VOLUME =====================
            if label == "Right":
                vol = np.interp(distance, [30, 300], [min_vol, max_vol])
                vol = np.clip(vol, min_vol, max_vol)
                volume.SetMasterVolumeLevel(vol, None)

                vol_percent = int(np.interp(distance, [30, 300], [0, 100]))
                cv2.putText(frame, f'Volume: {vol_percent}%',
                            (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2)

            # ===================== LEFT HAND → BRIGHTNESS =====================
            elif label == "Left" and monitors is not None:
                target_brightness = int(
                    np.clip(np.interp(distance, [30, 300], [0, 100]), 0, 100)
                )

                # Avoid flicker
                if abs(target_brightness - current_brightness) > 5:
                    try:
                        sbc.set_brightness(
                            target_brightness,
                            display=0,
                            method='wmi'
                        )
                        current_brightness = target_brightness
                    except Exception as e:
                        print("Brightness error:", e)

                cv2.putText(frame, f'Brightness: {target_brightness}%',
                            (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Volume & Brightness Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ===================== CLEANUP =====================
cap.release()
cv2.destroyAllWindows()
