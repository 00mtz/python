import cv2 as cv
from matplotlib import pyplot as plt
import os
import numpy as np

def da_hist (img, L = 256):
    shape_img = np.shape(img)
    h = np.zeros(L)

    for j in range(0, shape_img[1]):
        for i in range(0, shape_img[0]):
            if(img[i,j] != 0):
                h[img[i,j]] = h[img[i,j]] + 1

    p = np.divide(h,shape_img[0]*shape_img[1])

    return p

f = cv.imread('images/pompeiiFUCKTHETRAFO.png', cv.IMREAD_UNCHANGED)

L = 256
fk = range(0, L)