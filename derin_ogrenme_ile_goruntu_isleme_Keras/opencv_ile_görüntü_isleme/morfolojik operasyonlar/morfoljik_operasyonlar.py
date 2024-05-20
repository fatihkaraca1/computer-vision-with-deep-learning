import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("opencv_ile_görüntü_işleme\\bisiklet.jpg")
plt.figure(), plt.imshow(img, cmap= 'gray'), plt.axis("off"), plt.title("orjinal img")

#erezyon 
kernel = np.ones((5,5), dtype  = np.uint8)
result = cv2.erode(img, kernel, iterations=1)
plt.figure(), plt.imshow(result, cmap= 'gray'), plt.axis("off"), plt.title("erozyon")

#genişleme dilation
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure(), plt.imshow(result2, cmap= 'gray'), plt.axis("off"), plt.title("genişletme")

whiteNoise = np.random.randint(0,2, size  = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap= 'gray'), plt.axis("off"), plt.title("white noise")


plt.show()
