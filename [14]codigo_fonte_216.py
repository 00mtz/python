import numpy as np
import cv2 as cv

f = cv.imread('images/limiar.png', cv.IMREAD_GRAYSCALE)

threshold = 150

shape_f = np.shape(f)
g = np.zeros(shape_f)
for j in range(0, shape_f[1]):
    for i in range(0, shape_f[0]):
        if(f[i,j]<80):
            g[i,j] = 0
        else:
            g[i,j] = 255

cv.imwrite('output/limiarizacao_1.png', g)


g = (f >= threshold)*255

cv.imwrite('output/limiarizacao_x.png', g)