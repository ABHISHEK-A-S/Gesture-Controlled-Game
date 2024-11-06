import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller
import math
from keys import PressKey, W,A, D,S, Space, ReleaseKey

#global xl1,xl2,yl1,yl2,xr1,xr2,yr1,yr2

currentKey = list()
cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)


keyboard=Controller()

detector=HandDetector(detectionCon=0.8)

while True:
    key = False
    success, img=cap.read()

    img=cv2.flip(img,1)
    hands, img = detector.findHands(img)


    cv2.rectangle(img, (750, 300), (550, 100), (250, 100, 100),cv2.FILLED)
    cv2.rectangle(img, (750, 300), (550, 100), (255, 255, 0),5)
    cv2.putText(img, "W", (587, 250),cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 5)

    cv2.rectangle(img, (500, 550), (300, 350),(250, 100, 100), cv2.FILLED)
    cv2.rectangle(img, (500, 550), (300, 350), (255, 255, 0),5)
    cv2.putText(img, "A", (350, 500), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 5)

    cv2.rectangle(img, (750, 550), (550, 350), (250, 100, 100), cv2.FILLED)
    cv2.rectangle(img, (750, 550), (550, 350),  (255, 255, 0),5)
    cv2.putText(img, "S", (600, 500), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 5)

    cv2.rectangle(img, (1000, 550), (800 , 350), (250, 100, 100), cv2.FILLED)
    cv2.rectangle(img, (1000, 550), (800, 350), (255, 255, 0),5)
    cv2.putText(img, "D", (850, 500), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 5)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        xr1=lmList1[8][0]
        yr1 = lmList1[8][1]
        xr2 = lmList1[4][0]
        yr2 = lmList1[4][1]
        dist1=math.sqrt(math.pow(xr1-xr2,2)+math.pow(yr1-yr2,2))

        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            xl1 = lmList2[8][0]
            yl1 = lmList2[8][1]
            xl2 = lmList2[4][0]
            yl2 = lmList2[4][1]
            dist2 = math.sqrt(math.pow(xl1 - xl2, 2) + math.pow(yl1 - yl2, 2))

            if (550 < xr1 < 750 and 100 < yr1 < 300 and dist1 < 35) or (550 < xl1 < 750 and 100 < yl1 < 300 and dist2 < 35) :
                cv2.rectangle(img, (750, 300), (550, 100), (0, 255, 0),7)
                PressKey(W)
                key = True
                currentKey.append(W)

            if (300 < xr1 < 500 and 350 < yr1 < 550 and dist1 < 35) or (300 < xl1 < 500 and 350 < yl1 < 550 and dist2 < 35) :
                cv2.rectangle(img, (500, 550), (300, 350), (0, 255, 0),7)
                PressKey(A)
                key = True
                currentKey.append(A)



            if (550 < xr1 < 750 and 350 < yr1 < 550 and dist1 < 35) or (550 < xl1 < 750 and 350 < yl1 < 550 and dist2 < 35) :
                cv2.rectangle(img, (750, 550), (550, 350), (0, 255, 0),7)
                PressKey(S)
                key = True
                currentKey.append(S)

            if (800 < xr1 < 1000 and 350 < yr1 < 550 and dist1 < 35) or (800 < xl1 < 1000 and 350 < yl1 < 550 and dist2 < 35) :
                cv2.rectangle(img, (1000, 550), (800, 350), (0, 255, 0),7)

                PressKey(D)
                key = True
                currentKey.append(D)


            if not key and len(currentKey) != 0:
                for current in currentKey:
                    ReleaseKey(current)
                currentKey = list()

    #lmList,bboxInfo = detector.findHands(img)
    #plt.imshow(img[1])
    cv2.imshow("Image",img)
    cv2.waitKey(1)
