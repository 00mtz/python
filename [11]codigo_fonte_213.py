import cv2 as cv
import math
import os

img = cv.imread('images/pompei.jpg', cv.IMREAD_UNCHANGED)
img_rgb = cv.imread('images/feira.png', cv.IMREAD_UNCHANGED)

yc = math.floor(img.shape[0]/2)
xc = math.floor(img.shape[1]/2)

interval = 350 

img_sel = img[int(yc-interval/2):int(yc+interval/2), int(xc-interval/2):int(xc+interval/2)]

cv.imshow('Pompeii City', img)
cv.imshow('Pompeii City Selected', img_sel)

cv.imwrite('output/pompeii.png', img)
cv.imwrite('output/pompeii_city_selected.png', img_sel)

img_sel_rgb = img_rgb[0:10, 0:10, [0,2]]
print(img_sel_rgb.shape)

cv.waitKey(0)
cv.destroyAllWindows()