# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("forma.png")


print(img.shape)


rows,cols = img.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)

img_rotation = cv2.warpAffine(img,rotation_matrix,(int (cols*1.2) ,int (rows*1.2)))


cv2.imshow("forma",img)
cv2.imshow("rotated image",img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()
