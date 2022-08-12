import cv2 as cv
import numpy as np


img = cv.imread('images/canny2.png', cv.IMREAD_UNCHANGED)

img_edges = cv.Canny(img,100,200)

cv.imwrite('output/cannyzed2.png', img_edges)