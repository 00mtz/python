import cv2 as cv
import numpy as np

im_br = cv.imread('output/pompei_blurried.jpg', cv.IMREAD_UNCHANGED)

mask = np.array([[0,1,0],[1,-4,1],[0,1,0]],np.float32)

im_tr = cv.filter2D(im_br.astype(np.float32), -1, mask)

c = -1
im_agc = im_br + c*im_tr

cv.imwrite('output/pompei_sharpened.jpg', im_agc)

cv.imshow('teste 1', im_tr)
cv.waitKey(0)
cv.destroyAllWindows()