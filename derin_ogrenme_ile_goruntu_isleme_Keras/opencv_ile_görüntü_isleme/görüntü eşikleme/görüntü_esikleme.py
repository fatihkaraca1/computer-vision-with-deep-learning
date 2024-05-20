import cv2
import matplotlib.pyplot as plt

img = cv2.imread("bisiklet.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap= 'gray')
plt.axis("off")
plt.show()

_,thresh = cv2.threshold(img, thresh = 60, maxval = 255, type  = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh, cmap= 'gray')
plt.axis("off")
plt.show()

_,thresh = cv2.threshold(img, thresh = 60, maxval = 255, type  = cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

plt.figure()
plt.imshow(thresh, cmap= 'gray')
plt.axis("off")
plt.show()
