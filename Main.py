# -*- coding: utf-8 -*-
from SnakeGameClass import *
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the frame
cap.set(4, 1024)  # Set the height of the frame
detector = HandDetector(detectionCon=0.8, maxHands=1)
game = SnakeGameClass("donut.png")

while True:
    success, img = cap.read()

    if not success:
        print("Failed to read a frame from the camera.")
        break

    img = cv2.flip(img, 1)  # Flip the frame horizontally
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]["lmList"]
        pointIndex = lmList[8][0:2]
        img = game.update(img, pointIndex)

    cv2.imshow("img", img)

    if cv2.waitKey(1) == ord('r'):
        game.gameOver = False
        game.score = 0

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
