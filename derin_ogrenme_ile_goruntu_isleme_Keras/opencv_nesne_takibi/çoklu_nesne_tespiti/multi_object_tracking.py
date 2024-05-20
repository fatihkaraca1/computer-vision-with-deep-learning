#kodu python 3.6 sürümü ile açtım

import cv2

# OpenCV'de kullanılacak obje takipçileri ve oluşturucu fonksiyonları
OPENCV_OBJECT_TRACKERS = {
    "csrt"      : cv2.TrackerCSRT_create,
    "kcf"       : cv2.TrackerKCF_create,
    "boosting"  : cv2.TrackerBoosting_create,
    "mil"       : cv2.TrackerMIL_create,
    "tld"       : cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse"     : cv2.TrackerMOSSE_create
}

# Takipçinin adı
tracker_name = "boosting"

# Çoklu takipçi nesnesi oluşturuluyor
trackers = cv2.MultiTracker_create()

# Video dosyasının yolu
video_path = "opencv_nesne_takibi\\çoklu_nesne_tespiti\\MOT17-04-DPM.mp4"
cap = cv2.VideoCapture(video_path)

# Video FPS değeri
fps = 30     
f = 0
while True:
    
    # Video çerçevesini oku
    ret, frame = cap.read()
    (H, W) = frame.shape[:2]
    frame = cv2.resize(frame, dsize=(960, 540))
    
    # Takipçileri güncelle
    (success, boxes) = trackers.update(frame)
    
    # Bilgilerin listesi
    info = [("Tracker", tracker_name),
            ("Success", "Yes" if success else "No")]
    
    # Metin formatına dönüştürme
    string_text = ""
    for (i, (k, v)) in enumerate(info):
        text = "{}: {}".format(k, v)
        string_text = string_text + text + " "
    
    # Bilgileri çerçeveye ekleme
    cv2.putText(frame, string_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    # Kutuları çerçeveye ekleme
    for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Çerçeveyi gösterme
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    # Takipçi eklemek için "t" tuşuna basın
    if key == ord("t"):
        box = cv2.selectROI("Frame", frame, fromCenter=False)
        tracker = OPENCV_OBJECT_TRACKERS[tracker_name]()
        trackers.add(tracker, frame, box)
    
    # Çıkış için "q" tuşuna basın
    elif key == ord("q"):
        break

    f = f + 1
    
# Video yakalama nesnesini serbest bırak
cap.release()
cv2.destroyAllWindows() 
