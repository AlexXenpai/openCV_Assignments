# -*- coding: utf-8 -*-

import cv2


griResim = cv2.imread("balon.jpg",0)



cv2.imshow("gri ekran resmi", griResim)



resim = cv2.imread("balon.jpg")

cv2.imshow("ekran resmi", resim )


k = cv2.waitKey(0) & 0XFF
 


if   k == ord("q"):
    print("q tuşuna basarak resmi kapatabilirsiniz")
    cv2.destroyWindow("ekran resmi")
    
elif k == ord("s"):
    print("s tusuna basildi resim kaydedildi")
    cv2.imwrite("balon17.jpg", resim)
    cv2.destroyWindow("ekran resmi")    
if cv2.waitKey(0) == ord("c"):
    print("c tusuna basildi gri resim kapatildi")
    cv2.destroyWindow("gri ekran resmi")







