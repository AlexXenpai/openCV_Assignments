# -*- coding: utf-8 -*-

import cv2

import numpy as np

cv2.namedWindow("kamera",cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(0)


print("genislik degeri",cam.get(3))
print("uzunluk degeri",cam.get(4))
print("fps degeri",cam.get(5))

#cam.set boyut ayarlama


if not cam.isOpened():
    print("kamera tanınmadı")
    exit()

while True:
    ret, frame = cam.read()
    
    
    cv2.line(frame,(0,0), (511,511),(255,255,0),4)
    cv2.circle(frame,(100,100),90, 255,5)
    cv2.rectangle(frame,(50,50),(155,155),(0,0,255),5)
    cv2.putText(frame,"icardi",(150,150),0,4 ,(0,255,255),5,cv2.LINE_4)
    if not ret:
        print("kameradan görüntü alınamıyor")
        break
    
    cv2.imshow("kamera", frame)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        print("görüntü sonlandirildi.")
        break

cam.release()
cv2.destroyAllWindows()
