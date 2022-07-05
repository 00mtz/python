import cv2 as cv
from matplotlib import pyplot as plt
import os

img_rgb = cv.imread('images/feira.png', cv.IMREAD_UNCHANGED)

img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
_, img_bin = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

images = [img_rgb, img_gray, img_bin]
color_map = [None,'gray','gray']

fig = plt.figure()

plot_count =1
for img in images:
    ax = fig.add_subplot(1, len(images),plot_count)
    ax.imshow(img, cmap=color_map[plot_count-1], vmin=0, vmax=255)
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(False)
    plot_count=plot_count+1

fig.savefig('output/rgb_gray_binary_images.png', dpi=300, bbox_inches='tight')

plt.show()