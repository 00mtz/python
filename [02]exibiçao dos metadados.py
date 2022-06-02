import cv2 as cv 

img = cv.imread('C:/Users/OFICINAS06/Pictures/almoco.webp', cv.IMREAD_UNCHANGED)

print(img.shape)
print(type(img))
print(img.dtype)