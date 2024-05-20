import cv2
import numpy as np


image = cv2.imread("odev2.jpg",0)


cv2.imshow('Odev-2',image)


edges = cv2.Canny(image = image, threshold1 = 200, threshold2 = 255)
cv2.imshow('Kenar Tespiti',edges)


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


face_rect = face_cascade.detectMultiScale(image)
for (x,y,w,h) in face_rect:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),10)
cv2.imshow("Yuz Tespiti", image)


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


(rects, weights) = hog.detectMultiScale(image, padding=(8, 8), scale=1.05)

for (xA, yA, xB, yB) in rects:
    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 0, 255), 2)
	
cv2.imshow("insan Tespiti", image)
