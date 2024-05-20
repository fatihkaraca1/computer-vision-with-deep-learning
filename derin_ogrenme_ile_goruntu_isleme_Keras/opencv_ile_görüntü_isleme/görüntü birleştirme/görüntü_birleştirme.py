import cv2
import numpy as np

img = cv2.imread("bisiklet.jpg")
cv2.imshow("orjinal", img)

#yatay
hor = np.hstack((img,img))
cv2.imshow("horizontonal",hor)

#dikey
ver = np.vstack((img,img))
cv2.imshow("horizontonal",ver)
