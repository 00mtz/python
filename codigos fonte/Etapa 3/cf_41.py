import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv.imread('images/chaves.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 5)

for(x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    cv.imwrite('output/facesdetected.png', img)
