import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:/Users/OFICINAS06/Pictures/pompei.jpg', cv.IMREAD_UNCHANGED)

plt.imshow(img, cmap = 'gray')
plt.colorbar(cmap = 'gray', fraction = 0.3, pad = 0.4)
plt.show()