import cv2 as cv

img = cv.imread('./images/almoco.webp', cv.IMREAD_UNCHANGED)
cv.imshow('Almoco', img)

cv.waitKey(0)

cv.destroyAllWindows()
