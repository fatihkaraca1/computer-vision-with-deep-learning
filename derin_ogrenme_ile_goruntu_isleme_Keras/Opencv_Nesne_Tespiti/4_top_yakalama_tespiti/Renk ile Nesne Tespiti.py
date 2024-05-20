import cv2
import numpy as np
from collections import deque

# Nesne merkezini depolamak için deque kullanıyoruz
buffer_size = 16
pts = deque(maxlen=buffer_size)

# Mavi renk aralığı HSV'de tanımlanıyor
blueLower = (84,  98,  0)
blueUpper = (179, 255, 255)

# Kamera yakalama başlatılıyor
cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 480)

while True:
    
    success, imgOriginal = cap.read()
    
    if success: 
        
        # Görüntüyü bulanıklaştırma
        blurred = cv2.GaussianBlur(imgOriginal, (11, 11), 0) 
        
        # HSV renk uzayına dönüştürme
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        # Mavi renk için bir maske oluşturma
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        
        # Maskenin etrafındaki gürültüyü kaldırma
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        # Konturları bulma
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None

        if len(contours) > 0:
            
            # En büyük konturu seçme
            c = max(contours, key=cv2.contourArea)
            
            # Konturu çevreleyen dikdörtgeni bulma
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            
            # Bilgileri formatlayıp yazdırma
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x), np.round(y), np.round(width), np.round(height), np.round(rotation))
            print(s)
            
            # Dikdörtgeni çizme
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            cv2.drawContours(imgOriginal, [box], 0, (0, 255, 255), 2)
            
            # Merkezi bulma ve çizme
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(imgOriginal, center, 5, (255, 0, 255), -1)
            
            # Bilgileri ekrana yazdırma
            cv2.putText(imgOriginal, s, (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
            
        # Merkezi deque'ye ekleme
        pts.appendleft(center)
        
        # Önceki ve şu anki konumları birleştirme ve çizgi çizme
        for i in range(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None: 
                continue
            cv2.line(imgOriginal, pts[i - 1], pts[i], (0, 255, 0), 3)
        
        # Sonuçları gösterme
        cv2.imshow("Orijinal Tespit", imgOriginal)
        
    # Çıkış tuşuna basıldığında döngüyü kırma
    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break
