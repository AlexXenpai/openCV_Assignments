# -*- coding: utf-8 -*-

import cv2

import numpys as np


def draw(event,x,y,flags,param):
    
    if event ==









img = np.ones((512,512,3),np.uint8)

cv2.namedWindow("resim")
cv2.setMouseCallback("resim",draw)

