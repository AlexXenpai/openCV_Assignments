# -*- coding: utf-8 -*-

import cv2 




def nothing(x):
    pass

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("kaydedilen0",fourcc,30.0,(1376,768))

cv2.createTrackbar("R", "video", 0, 255, nothing)
cv2.createTrackbar("G", "video", 0, 255, nothing)
cv2.createTrackbar("B", "video", 0, 255, nothing)

while cam.isOpened():
    ret,frame = cam.read()
    
    if not ret:
        print("kameradan görüntü alınamadı")
        break
    
    out.write(frame)
    
    cv2.imshow("kamera",frame)
    
    
    if cv2.waitKey(1)== ord("q"):
        print("video bitti")
        break
    
    
    r = cv2.getTrackbarPos("R", "video")
    g = cv2.getTrackbarPos("G", "video")
    b = cv2.getTrackbarPos("B", "video")
    
    switch = cv2.getTrackbarPos("ON/OFF", "video")
    
    cam[:] = [b,g,r]
    
    
    
cam.release()
out.release()
cv2.destroyAllWindows()
    