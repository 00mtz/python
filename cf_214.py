from PIL import Image
import os

from cv2 import IMWRITE_JPEG_CHROMA_QUALITY

img = Image.open('images/feira.png')

region = (20, 20, 100, 100)
img_crop = img.crop(region)

img_rot = img.rotate(45)

img_crop.show(title= 'Feira cortada')
img_rot.show(title= 'Feira Rotacionada')

img_crop.save('output/feiracortada.png')
img_rot.save('output/feirarotacionada.png')