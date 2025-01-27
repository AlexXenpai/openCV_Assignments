
# -*- coding: utf-8 -*-
import cv2

import numpy as np



camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("kaydedilen1.mp4",fourcc,30.0,(640,480))

def nothing(x):
    pass


lower = np.array([87,50,50])
upper = np.array([110,255,255])




while camera.isOpened():
    _, frame = camera.read()
    
    
    
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    
    
    mask = cv2.inRange(hsv, lower, upper)
    
    res = cv2.bitwise_and(frame, frame,mask=mask)
    
   
    
    cv2.imshow("frame", frame)
    cv2.imshow("hsv", mask)
    cv2.imshow("res", res)
    out.write(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        print(contour)
        
        if area > 1000:
            cv2.drawContours(frame, contours,-1,(0,0,255),2)
            cv2.rectangle(frame,(contour[0][0],contour[0][1]),(contour[1][0],contour[1][1]),(0,255,0),2)
        
    
    
    
    
    if cv2.waitKey(1) == ord("q"):
        break
        
        
        
camera.release()

      
cv2.destroyAllWindows()
        
        
        
        
        
    
