# -*- coding: utf-8 -*-

import cv2

from matplotlib import pyplot as plt

resim = cv2.imread("IMG-20241212-WA0007.jpg")


cv2.namedWindow("resim penceresi",cv2.WINDOW_NORMAL)


cv2.imshow("resim penceresi",resim)

plt.imshow(resim)
plt.show()




k = cv2.waitKey(0)


if k == 27 :
    print("esc tuşuna basıldı")
    
elif k == ord("q"):
    print("q tuşuna basıldı resim kaydedildi")
    cv2.imwrite("IMG-20241212-WA0007.jpg", resim)
    
cv2.destroyAllWindows()