import cv2 as cv
import numpy as np

f = cv.imread('images/ruins.jpg', cv.IMREAD_UNCHANGED)

mask = np.ones((3,3), np.float32)/9

g = cv.filter2D(f, -1, mask)

cv.imwrite('output/pompei_blurried.jpg', g)

