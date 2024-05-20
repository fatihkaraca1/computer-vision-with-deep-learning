import numpy as np
import os
import cv2

# Nesne sınıfları
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

# Sınıfların rastgele renklerle eşleştirilmesi
COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))

# Önceden eğitilmiş SSD modelinin yüklenmesi
net = cv2.dnn.readNetFromCaffe("evrisimsel_sinir_aglari_nesne_tespiti\\ssd\\MobileNetSSD_deploy.prototxt.txt", "evrisimsel_sinir_aglari_nesne_tespiti\\ssd\\MobileNetSSD_deploy.caffemodel")

# Video akışının başlatılması
vc = cv2.VideoCapture(0) # Kameranın 0. porttan okunması (eğer birden fazla kamera varsa, port numarasını değiştirin)
vc.set(3,800) # Genişlik ayarı
vc.set(4,600) # Yükseklik ayarı
        
while True:
    
    # Kameradan bir kare yakalanması
    success, image = vc.read()
    (h,w) = image.shape[:2]
    
    # Görüntünün ağı blob'una dönüştürülmesi
    blob = cv2.dnn.blobFromImage(cv2.resize(image,(300, 300)), 0.007843,(300, 300), 127.5)
    
    # Ağa girişin sağlanması ve nesne tespitinin yapılması
    net.setInput(blob)
    detections = net.forward()
    
    # Algılanan nesnelerin işlenmesi ve çevresine dikdörtgen çizilmesi
    for j in np.arange(0, detections.shape[2]):
        
        confidence = detections[0,0,j,2]
        
        # Algılama güven değeri eşik değerinden büyükse
        if confidence > 0.10:
            
            idx = int(detections[0,0,j,1])
            box = detections[0,0,j,3:7]*np.array([w,h,w,h])
            (startX, startY, endX, endY) = box.astype("int")
            
            label = "{}: {}".format(CLASSES[idx], confidence)
            
            # Algılanan nesnenin çevresine dikdörtgen çizilmesi ve etiketin eklenmesi
            cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx],2)
            y = startY - 16 if startY -16 >15 else startY + 16
            cv2.putText(image, label, (startX,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5,COLORS[idx],2)
            
    
    cv2.imshow("ssd",image)
    if cv2.waitKey(1) & 0xFF == ord("q"): break  # q tuşuna basıldığında döngünün sonlandırılması
    

cv2.destroyAllWindows()
