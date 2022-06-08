import numpy as np
import cv2 as cv

f = cv.imread('images/contraste.png', cv.IMREAD_UNCHANGED)

f1 = 100
g1 = 50
f2 = 150
g2 = 200
L = 256

shape_f = np.shape(f)
g = np.zeros(shape_f)
for j in range(0, shape_f[1]):
    for i in range(0, shape_f[0]):
        