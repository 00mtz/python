import cv2 as cv
import numpy as np


img = cv.imread('images/canny2.png', cv.IMREAD_UNCHANGED)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_gray = np.float32(img_gray)
img_corners = cv.cornerHarris(img_gray,2,3,0.04)

img_corners = cv.dilate(img_corners, None, iterations=10)

img[img_corners>0.01*img_corners.max()]=[0,0,255]

cv.imwrite('output/chessboard_corners.png', img)