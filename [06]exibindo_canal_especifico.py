import cv2 as cv 

img = cv.imread('C:/Users/OFICINAS06/Pictures/frutas.jpg', cv.IMREAD_UNCHANGED)
cv.imshow('Street Italy Market', img[:, :, 2])

cv.waitKey(0)
cv.destroyAllWindows