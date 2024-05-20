import cv2

# Tanımlamalar
objectName = "Kalem Ucu"  # Tespit edilecek nesnenin adı
frameWidth = 280  # Kameradan alınacak görüntünün genişliği
frameHeight = 360  # Kameradan alınacak görüntünün yüksekliği
color = (255,0,0)  # Çerçeve ve metin rengi

# Kamera bağlantısı
cap = cv2.VideoCapture(0)  # Kameraya bağlan
cap.set(3,frameWidth)  # Görüntünün genişliğini ayarla
cap.set(4,frameHeight)  # Görüntünün yüksekliğini ayarla

def empty(a):  # Boş bir fonksiyon tanımla (Trackbar için gereklidir)
    pass

# Trackbar'ı oluştur
cv2.namedWindow("Sonuc")  # Sonuc penceresini oluştur
cv2.resizeWindow("Sonuc", frameWidth, frameHeight + 100)  # Pencerenin boyutunu ayarla
cv2.createTrackbar("Scale","Sonuc",400,1000,empty)  # Scale trackbar'ını oluştur
cv2.createTrackbar("Neighbor","Sonuc",4,50,empty)  # Neighbor trackbar'ını oluştur

# Cascade sınıflandırıcıyı yükle
cascade = cv2.CascadeClassifier("Opencv_Nesne_Tespiti\\10_custom_cascade\\cascade.xml")  # Cascade sınıflandırıcıyı yükle

while True:
    
    # Görüntüyü oku
    success, img = cap.read()  # Kameradan bir kare al
    
    if success:
        # Görüntüyü gri tona dönüştür
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tona dönüştür
        
        # Tespit parametreleri
        scaleVal = 1 + (cv2.getTrackbarPos("Scale","Sonuc")/1000)  # Ölçek değerini al
        neighbor = cv2.getTrackbarPos("Neighbor","Sonuc")  # Neighbor değerini al
        
        # Nesne tespiti
        rects = cascade.detectMultiScale(gray, scaleVal, neighbor)  # Nesneleri tespit et
    
        # Tespit edilen nesnelerin çevresine dikdörtgen çiz
        for (x,y,w,h) in rects:
            cv2.rectangle(img, (x,y),(x+w,y+h), color, 3)  # Dikdörtgen çiz
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)  # Metni ekle
            
        # Sonucu göster
        cv2.imshow("Sonuc", img)  # Sonucu göster
    
    # Çıkış için q tuşuna basılmasını kontrol et
    if cv2.waitKey(1) & 0xFF == ord("q"):  # q tuşuna basıldığında çıkış yap
        break
    
# Kamera bağlantısını serbest bırak
cap.release()  
cv2.destroyAllWindows()  
