import cv2
import os

# Bulunduğunuz dizindeki dosyaları listele
os.chdir("Opencv_Nesne_Tespiti\\11_Pedestrian Detection OpenCV")
files = os.listdir()
img_path_list = []

# .jpg uzantılı dosyaların yollarını bir listede topla
for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
    
print(img_path_list)

# HOG tanımlayıcısı oluştur
hog = cv2.HOGDescriptor()
# SVM tabanlı insan tanımlayıcıyı HOG tanımlayıcısına ekle
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Her bir resim dosyası için işlem yap
for imagePath in img_path_list:
    print(imagePath)
    
    # Resmi oku
    image = cv2.imread(imagePath)
    
    # İnsanları tespit et
    (rects, weights) = hog.detectMultiScale(image, padding=(8,8), scale=1.05)
    
    # Tespit edilen insanları dikdörtgenlerle çevrele
    for (x,y,w,h) in rects:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
         
    # Sonucu göster
    cv2.imshow("Yaya: ", image)
    
    # q tuşuna basıldığında sonraki resme geç
    if cv2.waitKey(0) & 0xFF == ord("q"):
        continue

# Pencereleri kapat
cv2.destroyAllWindows()
