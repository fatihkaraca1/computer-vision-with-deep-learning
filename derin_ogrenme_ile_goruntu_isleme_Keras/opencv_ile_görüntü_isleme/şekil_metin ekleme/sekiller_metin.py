import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8) #siyah bir resim oluştur

cv2.imshow("siyah",img)

#cizgi

cv2.line(img, (0,0), (512,512), (0,255,0)) 
# resim, başlangıç noktası, bitiş noktaları, renk, kalınlık
cv2.imshow("cizgi", img)

cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("dikdörtgen", img)

cv2.circle(img, (300,300), 45,(0,0,255), cv2.FILLED)
cv2.imshow("cember", img)


cv2.putText(img, "resim",(350,350),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("metin", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
