import cv2
import matplotlib.pyplot as plt
import numpy as np

# Resmi içe aktar ve gri tonlamaya dönüştür
img = cv2.imread("Opencv_Nesne_Tespiti\\2_kose_tespiti\\sudoku.jpg", 0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# Harris köşe tespiti
dst = cv2.cornerHarris(img, blockSize=2, ksize=3, k=0.04)
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

# Köşeleri genişletme
dst = cv2.dilate(dst, None)
img[dst > 0.2 * dst.max()] = 1
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

# Shi-Tomasi köşe tespiti
img = cv2.imread("sudoku.jpg", 0)  # Resmi yeniden yükle
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 120, 0.01, 10)  # Köşeleri tespit et
corners = np.int64(corners)

# Köşeleri dairelerle işaretle
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (125, 125, 125), cv2.FILLED)

# Sonucu göster
plt.imshow(img)
plt.axis("off")
plt.show()
