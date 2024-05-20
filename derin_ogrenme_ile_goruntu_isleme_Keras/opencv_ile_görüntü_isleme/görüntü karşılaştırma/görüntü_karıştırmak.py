import cv2
import matplotlib as plt

img_1 = cv2.imread("img1.jpg")
img_2 = cv2.imread("img2.jpg")

plt.figure()
plt.imshow(img_1)

plt.figure()
plt.imshow(img_2)

img_1 = cv2.resize(img_1,(600,600))
img_2 = cv2.resize(img_2,(600,600))

plt.figure()
plt.imshow(img_1)

plt.figure()
plt.imshow(img_2)

blended = cv2.addWeighted(src1= img_1, alpha = 0.5, src2=img_2, beta = 0.5, gamma=0.5)
plt.figure()
plt.imshow(blended)

