import numpy as np
import math as mt
import cv2 as cv

cap = cv.VideoCapture('videos/video.mp4')

fps = int(cap.get(cv.CAP_PROP_FPS))
number_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

count = 0

while(count<number_frames):
    ret, frame = cap.read()

    cv.imshow('frame',frame)
    if cv.waitKey(int(mt.floor(1000/fps))) & 0xFF == ord('q'):
        break
    count = count + 1

cap.realease()
cv.destroyAllWindows()