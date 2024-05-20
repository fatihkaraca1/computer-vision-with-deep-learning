import cv2
import os
from os.path import isfile, join
import matplotlib.pyplot as plt

# Görüntülerin bulunduğu dizinin yolu
pathIn = r'opencv_nesne_takibi\\diğer_takip_algoritmaları\\img1'
# Çıkış videosunun kaydedileceği yol
pathOut = "opencv_nesne_takibi\\diğer_takip_algoritmaları\\MOT17-13-SDP.mp4"

# Belirtilen dizindeki tüm dosyaları listeleyin
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]

# Örnek bir görüntüyü okuyup göstermek için 
# img = cv2.imread(pathIn + "\\"+files[44])
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)

# Videonun fps (frame per second) değeri
fps = 25

size = (1920,1080)
# Video yazıcı oluşturma (MP4V codec, belirlenen fps ve boyutta)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*"MP4V"), fps, size, True)

# Dosya isimleri üzerinde döngü
for i in files:
    print(i)  # Hangi dosyanın işlendiğini yazdır

    # Her dosyanın tam yolunu oluştur
    filename = pathIn + "\\" + i
    
    #oku
    img = cv2.imread(filename)
    
    #videoya yaz
    out.write(img)

# Video dosyasını serbest bırak
out.release()
