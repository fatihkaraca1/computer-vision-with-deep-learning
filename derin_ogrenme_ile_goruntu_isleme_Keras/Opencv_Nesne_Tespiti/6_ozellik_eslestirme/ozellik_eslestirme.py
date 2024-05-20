import cv2
import matplotlib.pyplot as plt

# Ana görüntüyü içe aktar
chos = cv2.imread("Opencv_Nesne_Tespiti\\6_ozellik_eslestirme\\chocolates.jpg", 0)
plt.figure(), plt.imshow(chos, cmap="gray"), plt.axis("off")

# Aranacak olan görüntü
cho = cv2.imread("Opencv_Nesne_Tespiti\\6_ozellik_eslestirme\\nestle.jpg", 0)
plt.figure(), plt.imshow(cho, cmap="gray"), plt.axis("off")

# ORB tanımlayıcı
orb = cv2.ORB_create()

# Anahtar nokta tespiti ORB ile
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

# BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
# Noktaları eşleştir
matches = bf.match(des1, des2)

# Mesafeye göre sırala
matches = sorted(matches, key=lambda x: x.distance)

# Eşleşen resimleri görselleştirelim
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags=2)
plt.imshow(img_match), plt.axis("off"), plt.title("ORB")

# BRISK tanımlayıcı
brisk = cv2.BRISK_create()

# Anahtar nokta tespiti BRISK ile
kp1, des1 = brisk.detectAndCompute(cho, None)
kp2, des2 = brisk.detectAndCompute(chos, None)

# BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
# Noktaları eşleştir
matches = bf.match(des1, des2)

# Mesafeye göre sırala
matches = sorted(matches, key=lambda x: x.distance)

# Eşleşen resimleri görselleştirelim
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags=2)
plt.imshow(img_match), plt.axis("off"), plt.title("BRISK")

# AKAZE tanımlayıcı
akaze = cv2.AKAZE_create()

# Anahtar nokta tespiti AKAZE ile
kp1, des1 = akaze.detectAndCompute(cho, None)
kp2, des2 = akaze.detectAndCompute(chos, None)

# BFMatcher
bf = cv2.BFMatcher()
# Noktaları eşleştir
matches = bf.knnMatch(des1, des2, k=2)

guzel_eslesme = []

for match1, match2 in matches:
    if match1.distance < 0.75 * match2.distance:
        guzel_eslesme.append([match1])

# Eşleşen resimleri görselleştirelim
plt.figure()
img_match = cv2.drawMatchesKnn(cho, kp1, chos, kp2, guzel_eslesme, None, flags=2)
plt.imshow(img_match), plt.axis("off"), plt.title("AKAZE")

plt.show()
