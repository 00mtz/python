import cv2 as cv

img = cv.imread('./images/declaracao de amor.png', cv.IMREAD_UNCHANGED)
cv.imshow('Almoco', img)

cv.waitKey(0)

cv.destroyAllWindows()
