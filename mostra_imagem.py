import cv2 as cv

img = cv.imread('C:/Users/OFICINAS06/Pictures/estrogonofe-tradicional-rapido.webp', cv.IMREAD_UNCHANGED)
cv.imshow('Almoço', img)

cv.waitKey(0)

cv.destroyAllWindows
