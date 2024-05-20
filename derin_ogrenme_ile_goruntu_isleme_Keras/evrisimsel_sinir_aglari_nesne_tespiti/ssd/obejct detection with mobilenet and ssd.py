import numpy as np
import os
import cv2

# Nesne tespiti için sınıf etiketleri
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

# Her sınıfa rastgele bir renk atanması
COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))

# Önceden eğitilmiş modelin yüklenmesi
net = cv2.dnn.readNetFromCaffe("evrisimsel_sinir_aglari_nesne_tespiti\\ssd\\MobileNetSSD_deploy.prototxt.txt", "evrisimsel_sinir_aglari_nesne_tespiti\\ssd\\MobileNetSSD_deploy.caffemodel")

# Çalışma dizininin değiştirilmesi için "chdir" kullandık
directory = "evrisimsel_sinir_aglari_nesne_tespiti//ssd"
os.chdir(directory)

# Dizindeki dosyaların listelenmesi
files = os.listdir()

# JPEG dosyalarının yolu için boş bir liste oluşturulması
img_path_list = []
for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
        

for i in img_path_list:
    
    
    image = cv2.imread(i)
    (h,w) = image.shape[:2]
    
    # Görüntünün ağı blob'una dönüştürülmesi
    blob = cv2.dnn.blobFromImage(cv2.resize(image,(300, 300)), 0.007843,(300, 300), 127.5)
    
    # Ağın girişinin ayarlanması
    net.setInput(blob)
    detections = net.forward()
    
    # Algılama sonuçlarının işlenmesi ve nesnelerin çevresine çerçeve çizilmesi
    for j in np.arange(0, detections.shape[2]):
        
        # Algılama güven değerinin alınması
        confidence = detections[0,0,j,2]
        
        # Güven değerinin belirlenen eşik değerinden büyük olup olmadığının kontrol edilmesi
        if confidence > 0.10:
            
            # Algılanan nesnenin sınıf indeksinin alınması
            idx = int(detections[0,0,j,1])
            
            # Algılanan nesnenin koordinatlarının alınması ve boyutlandırılması
            box = detections[0,0,j,3:7]*np.array([w,h,w,h])
            (startX, startY, endX, endY) = box.astype("int")
            
            # Sınıf etiketi ve güven değerinin metin olarak yazılması
            label = "{}: {}".format(CLASSES[idx], confidence)
            
            # Algılanan nesnenin çevresine dikdörtgen çizilmesi ve etiketin yazılması
            cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx],2)
            y = startY - 16 if startY -16 >15 else startY + 16
            cv2.putText(image, label, (startX,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5,COLORS[idx],2)
            
    
    cv2.imshow("ssd",image)
    if cv2.waitKey(0) & 0xFF == ord("q"): 
        break
    
cv2.destroyAllWindows()
