import numpy as np
import cv2 as cv

f = cv.imread('images/Umberto1.png', cv.IMREAD_UNCHANGED)

f_hsv = cv.cvtColor(f, cv.COLOR_BGR2HSV)

epsilon = np.finfo(float).eps

L = 256
c = (L-1)/np.log(L)
shape_f = np.shape(f)

g_hsv = f_hsv 
for j in range (0, shape_f[1]):
    for i in range (0, shape_f[0]):
        g_hsv[i,j,2] = c*np.log(f[i,j,2]+epsilon)

g = cv.cvtColor(g_hsv, cv.COLOR_HSV2BGR)

cv.imshow('obrigado', g)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('output/logaritmotransformado.png', g)