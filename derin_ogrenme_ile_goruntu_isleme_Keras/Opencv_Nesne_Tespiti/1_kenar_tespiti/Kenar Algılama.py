import cv2
import matplotlib.pyplot as plt
import numpy as np

# Resmi içe aktar
img = cv2.imread("Opencv_Nesne_Tespiti\\1_kenar_tespiti\\london.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# Kenarları algıla
edges = cv2.Canny(image=img, threshold1=0, threshold2=255)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

# Resmin piksel değerlerinin ortancasını hesapla
med_val = np.median(img)
print("Median değeri:", med_val)

# Kenar tespiti için düşük ve yüksek eşik değerlerini belirle
low = int(max(0, (1 - 0.33) * med_val))
high = int(min(255, (1 + 0.33) * med_val))
print("Düşük eşik değeri:", low)
print("Yüksek eşik değeri:", high)

# Yeniden kenarları algıla
edges = cv2.Canny(image=img, threshold1=low, threshold2=high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

# Görüntüyü bulanıklaştır
blurred_img = cv2.blur(img, ksize=(5, 5))
plt.figure(), plt.imshow(blurred_img, cmap="gray"), plt.axis("off")

# Bulanıklaştırılmış resmin piksel değerlerinin ortancasını hesapla
med_val = np.median(blurred_img)
print("Median değeri (bulanık):", med_val)

# Yeniden kenar tespiti için düşük ve yüksek eşik değerlerini belirle
low = int(max(0, (1 - 0.33) * med_val))
high = int(min(255, (1 + 0.33) * med_val))
print("Düşük eşik değeri (bulanık):", low)
print("Yüksek eşik değeri (bulanık):", high)

# Yeniden kenarları algıla (bulanık)
edges = cv2.Canny(image=blurred_img, threshold1=low, threshold2=high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

plt.show()
