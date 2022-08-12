import cv2 as cv
import numpy as np

img = cv.imread('images/sphere.png', cv.IMREAD_UNCHANGED)

struct_elem = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)

img_bdr = img - cv.erode(img, struct_elem, iterations= 1)

cv.imwrite('output/boundary.png', img_bdr)