# -*- coding: utf-8 -*-
import cv2

import numpy as np



camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("kaydedilen1.mp4",fourcc,30.0,(640,480))

def nothing(x):
    pass



cv2.namedWindow("frame")
cv2.createTrackbar("H1", "frame", 0, 179,nothing )
cv2.createTrackbar("H2", "frame", 179, 179,nothing )
cv2.createTrackbar("S1", "frame", 0, 255,nothing )
cv2.createTrackbar("S2", "frame", 255, 255,nothing )
cv2.createTrackbar("V1", "frame", 0, 255,nothing )
cv2.createTrackbar("V2", "frame", 255, 255,nothing )

while camera.isOpened():
    _, frame = camera.read()
    
    
    
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    H1 = cv2.getTrackbarPos("H1", "frame")
    H2 = cv2.getTrackbarPos("H2", "frame")
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")
    
    lower = np.array([H1,S1,V1])
    upper = np.array([H2,S2,V2])
    
    mask = cv2.inRange(hsv, lower, upper)
    
    res = cv2.bitwise_and(frame, frame,mask=mask)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        
        
        if area > 1000:
            
            
            
            x, y, w, h = cv2.boundingRect(contour)
            #cv2.drawContours(frame, [contour],-1,(0,0,255),2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255,0),2)
            
    
   
    
    cv2.imshow("frame", frame)
    cv2.imshow("hsv", mask)
    cv2.imshow("res", res)
    out.write(frame)
    
    
    
    
    
    
    if cv2.waitKey(1) == ord("q"):
        break
        
        
        
camera.release()

      
cv2.destroyAllWindows()
        
        
        
        
        
    