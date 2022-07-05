import numpy as np
import cv2 as cv

f = cv.imread('images/contraste.png', cv.IMREAD_GRAYSCALE)

f1 = 100
g1 = 50
f2 = 150
g2 = 200
L = 256

shape_f = np.shape(f)
g = np.zeros(shape_f)

print(shape_f)
print(type(f))
print(f)

for j in range(0, shape_f[1]):
    for i in range(0, shape_f[0]):
        if(f[i,j]<=f1):
            g[i,j]=f[i,j]*g1/f1
        elif(f[i,j]>f1 and f[i,j]<=f2):
            g[i,j]=(f[i,j]-f1)*(g2-g1)/(f2-f1)+g1
        elif(f[i,j]>f2):
            g[i,j]=(f[i,j]-f2)*((L-1)-g2)/((L-1)-f2)+g2

cv.imshow('teste', g)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('output/contrast_stretching.png', g)
        