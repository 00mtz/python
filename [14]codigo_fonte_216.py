import numpy as np
import cv2 as cv

f = cv.imread('images/limiar.png', cv.IMREAD_UNCHANGED)

threshold = 150

shape_f = np.shape(f)
g = np.zeros(shape_f)
for j in range(0, shape_f[1]):
    for i in range(0, shape_f[0]):
        if(f[i,j]<150):
            g[i,j] = 0
        else:
            g[i,j] = 255

cv.imwrite('output/limiarizacao_4.png', g)


#g = (f >= threshold)*255

#cv.imwrite('output/limiarizacao_2.png', g)