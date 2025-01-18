import cv2
import mediapipe as mp
import numpy as np
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialisation de la capture vidéo
cap = cv2.VideoCapture(0)

# Initialisation de mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                     max_num_hands=1,
                     min_detection_confidence=0.7,
                     min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Initialisation du contrôle du volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def count_fingers(hand_landmarks):
    """Compte le nombre de doigts levés"""
    fingers = []
    
    # Pouce
    if hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].x:
        fingers.append(1)
    else:
        fingers.append(0)
    
    # 4 autres doigts
    tips = [mpHands.HandLandmark.INDEX_FINGER_TIP, mpHands.HandLandmark.MIDDLE_FINGER_TIP,
            mpHands.HandLandmark.RING_FINGER_TIP, mpHands.HandLandmark.PINKY_TIP]
    pips = [mpHands.HandLandmark.INDEX_FINGER_PIP, mpHands.HandLandmark.MIDDLE_FINGER_PIP,
            mpHands.HandLandmark.RING_FINGER_PIP, mpHands.HandLandmark.PINKY_PIP]
    
    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)
    
    return sum(fingers)

while True:
    success, img = cap.read()
    if not success:
        break
        
    # Convertir l'image en RGB pour mediapipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Dessiner les points de repère de la main
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
            # Compter les doigts levés
            fingers_up = count_fingers(handLms)
            
            # Ajuster le volume en fonction du nombre de doigts
            if fingers_up == 5:
                volume.SetMasterVolumeLevelScalar(1.0, None)  # 100%
                vol_percentage = 100
            elif fingers_up == 4:
                volume.SetMasterVolumeLevelScalar(0.8, None)  # 80%
                vol_percentage = 80
            elif fingers_up == 3:
                volume.SetMasterVolumeLevelScalar(0.6, None)  # 60%
                vol_percentage = 60
            elif fingers_up == 2:
                volume.SetMasterVolumeLevelScalar(0.4, None)  # 40%
                vol_percentage = 40
            elif fingers_up == 1:
                volume.SetMasterVolumeLevelScalar(0.2, None)  # 20%
                vol_percentage = 20
            else:  # 0 doigts
                volume.SetMasterVolumeLevelScalar(0.0, None)  # 0%
                vol_percentage = 0
            
            # Afficher le nombre de doigts et le pourcentage du volume
            cv2.putText(img, f'Doigts: {fingers_up}', (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.putText(img, f'Volume: {vol_percentage}%', (10, 120),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    
    # Afficher l'image
    cv2.imshow('Hand Volume Control', img)
    
    # Quitter si 'q' est pressé
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
