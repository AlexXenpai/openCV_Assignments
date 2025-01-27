# -*- coding: utf-8 -*-

import cv2

import numpy as np


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)

cv2.line(img,(0,0), (511,511),(255,255,0),4)
cv2.circle(img,(100,100),90, 255,5)
cv2.rectangle(img,(50,50),(155,155),(0,0,255),5)
cv2.putText(img,"icardi",(150,150),0,4 ,(0,255,255),5,cv2.LINE_4)




cv2.imshow("img",img)
k = cv2.waitKey(0) 
cv2.destroyAllWindows()



