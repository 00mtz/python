import cv2 as cv 

img = cv.imread('./images/frutas.jpg', cv.IMREAD_UNCHANGED)
cv.imshow('Street Italy Market', img)

print(img.shape)
print(type(img))
print(img.dtype)

cv.waitKey(0)
cv.destroyAllWindows
