# -*- coding: utf-8 -*-


import cv2

cam = cv2.VideoCapture(0)


if not cam.isOpened():
    print("kamera okunmadı")
    exit()

while cam.isOpened():
    ret , frame = cam.read()
    
    frame = cv2.cvtColor(frame,0)
    flip = cv2.flip(frame,1)
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.line(frame,(0,0), (511,511),(255,255,0),4)
    cv2.imshow("kamera0", frame)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        print("gri video sonlandirildi")
        
        break
    
    
    cv2.imshow("kamera1",flip)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        print("renkli video sonlandirildi")
        
        break



cam.release()
cv2.destroyAllWindows()
    