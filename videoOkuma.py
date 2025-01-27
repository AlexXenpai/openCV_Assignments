# -*- coding: utf-8 -*-

import cv2

import numpy as np


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
    
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    
    if not ret:
        print("kameradan görüntü alınamıyor")
        break
    
    cv2.imshow("kamera", frame)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        print("görüntü sonlandirildi.")
        break

cam.release()
cv2.destroyAllWindows()
