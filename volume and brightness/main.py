import cv2 # For webcam and display
import mediapipe as mp # For hand detection
print("mediapipe installed")
import numpy as np # For number conversion
from math import hypot# To find distance between fingers
# Volume control (Windows)

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# Brightness control

import screen_brightness_control as sbc

mp_hands = mp.solutions.hands
hands =  mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

mp_draw = mp.solutions.drawing_utils
# Initialize Pycaw for volume control




try:

    # getting to know your computer speaker
    
    devices = AudioUtilities.GetSpeakers()
    #this connects python to the volume control system of your computer

    interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)
    #it gets permission to change your volume

    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    print("Current volume:", current_volume)
    # Set volume (0.0 to 1.0)
    volume.SetMasterVolumeLevelScalar(0.5, None)
    min_vol, max_vol = volume.GetVolumeRange()[0:2]

except Exception as e:

    print(f"Pycaw error: {e}")

    exit()
cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("Error: Webcam not accessible.")
    exit()
while True:

    ret, img = cap.read()
    if not ret:
        break
    img = cv2.flip(img,1)#Mirror effect
    img_color = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(img_color)
    # retrieve frame dimentions for dynamic bar positioning
    h,w,_= img.shape
    # Are there any hands in found in the captured video and if it is left or right
    if results.multi_hand_landmarks and results.multi_handedness:
        #go through each detected hand one by one
        for i, handLms in enumerate(results.multi_hand_landmarks):
            # i = hand number(0,1,2)
            #handLms = land marks (finger points)
            label = results.multi_handedness[i].classification[0].label # "Left" or "Right"
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            # Get thumb and index finger tips
            thumb = handLms.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index = handLms.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_pos = (int(thumb.x * w), int(thumb.y * h))
            index_pos = (int(index.x * w), int(index.y * h))
            cv2.circle(img, thumb_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos, (0, 255, 0), 3)
            # Calculate the Euclidean distance between thumb and index finger
            dist = hypot(index_pos[0] - thumb_pos[0], index_pos[1] - thumb_pos[1])

            if label == "Right":  # Volume control with right hand
                vol = np.interp(dist, [30, 300], [min_vol, max_vol])
                try:
                    volume.SetMasterVolumeLevel(vol, None)
                except Exception as e:
                    print(f"Volume error: {e}")
            elif label == "Left":  # Brightness control with left hand
                bright = np.interp(dist, [30, 300], [0, 100])
                try:
                    sbc.set_brightness(bright)
                except Exception as e:
                    print(f"Brightness error: {e}")

    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()