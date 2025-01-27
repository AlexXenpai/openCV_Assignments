import cv2
import  numpy as np


resim = cv2.imread("forma.png")
resim_hvs = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)

lower = np.array([38,100,100])
upper = np.array([75,255,255])

mask = cv2.inRange(resim_hvs,lower,upper)
res = cv2.bitwise_and(resim,resim,mask=mask)

cv2.imshow("son",res)
cv2.imshow("cvt",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()