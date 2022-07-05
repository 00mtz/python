import cv2 as cv 

img = cv.imread('./images/frutas.jpg', cv.IMREAD_UNCHANGED)
cv.imshow('Red', img[:, :, 2])
cv.imshow('Green', img[:, :, 1])
cv.imshow('Blue', img[:, :, 0])

cv.waitKey(0)
cv.destroyAllWindows
