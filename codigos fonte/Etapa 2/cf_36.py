import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt

img = cv.imread('images/vitral.png', cv.IMREAD_UNCHANGED)

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

shape_f = np.shape(img_hsv)
img_bin = np.zeros(shape_f[0:2])
for j in range(0, shape_f[1])
    for i in range(0,shape_f[0])
        if(img_hsv[i,j,0]>102
        and img_hsv[i,j,0]<138
        and img_hsv[i,j,1]>50
        and img_hsv[i,j,2]>50)
