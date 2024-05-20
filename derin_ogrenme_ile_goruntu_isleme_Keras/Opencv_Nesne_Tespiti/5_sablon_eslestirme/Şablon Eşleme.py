import cv2
import matplotlib.pyplot as plt

# Resimleri yükleme
img = cv2.imread("Opencv_Nesne_Tespiti\\5_sablon_eslestirme\\cat.jpg", 0)
template = cv2.imread("Opencv_Nesne_Tespiti\\5_sablon_eslestirme\\cat_face.jpg", 0)

# Resim boyutlarını yazdırma
print(img.shape)
print(template.shape)

h, w = template.shape
# Sablon ve görüntü arasındaki farklı metotlar
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# Her bir metot için işlem yapma
for meth in methods:
    
    method = eval(meth) # 'cv2.TM_CCOEFF' -> cv2.TM_CCOEFF
    
    # Sablon eşleştirmesi yapma
    res = cv2.matchTemplate(img, template, method)
    print(res.shape)
    
    # Eşleşme sonucunun en küçük ve en büyük değerlerini bulma
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # Eğer metot 'cv2.TM_SQDIFF' veya 'cv2.TM_SQDIFF_NORMED' ise en küçük konumu kullanma
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    
    # Kare çizme için köşe noktalarını bulma
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    # Tespit edilen yüzü kare içine alma
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    
    # Eşleşme sonucunu ve tespit edilen yüzü görselleştirme
    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap="gray")
    plt.title("Eşleşme Sonucu"), plt.axis("off")
    plt.subplot(122), plt.imshow(img, cmap="gray")
    plt.title("Tespit Edilen Sonuç"), plt.axis("off")
    plt.suptitle(meth)
    
    # Görselleri gösterme
    plt.show()
