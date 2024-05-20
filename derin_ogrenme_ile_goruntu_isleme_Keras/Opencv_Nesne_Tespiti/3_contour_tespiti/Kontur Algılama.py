import cv2
import matplotlib.pyplot as plt
import numpy as np

# Resmi içe aktar
img = cv2.imread("Opencv_Nesne_Tespiti\\3_contour_tespiti\\contour.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# Farklı sürüm için 
# image, contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Görüntüdeki konturları bul
contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Dış ve iç konturları depolamak için sıfırlarla dolu bir dizi oluştur
external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

# Tüm konturları dolaş
for i in range(len(contours)):
    
    # Konturun dış kontur olup olmadığını kontrol et
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contour, contours, i, 255, -1) # Dış kontur çizimi
    else: # İç kontur
        cv2.drawContours(internal_contour, contours, i, 255, -1) # İç kontur çizimi

# Dış konturu görselleştir
plt.figure(), plt.imshow(external_contour, cmap="gray"), plt.axis("off")
# İç konturu görselleştir
plt.figure(), plt.imshow(internal_contour, cmap="gray"), plt.axis("off")
