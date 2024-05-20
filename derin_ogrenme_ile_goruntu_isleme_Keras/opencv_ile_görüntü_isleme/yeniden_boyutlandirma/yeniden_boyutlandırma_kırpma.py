import cv2

img = cv2.imread("opencv_ile_görüntü_isleme\yeniden_boyutlandirma\lenna.png",0)
# print("resim-boyutu: ",img.shape)
cv2.imshow("orjinal",img)

img_resized = cv2.resize(img, (800,800))
print("resized img shape: ", img_resized.shape)
cv2.imshow("img resized", img_resized)

# kırp

img_croped = img[:200,:300]  #width -> height
cv2.imshow("cropped img", img_croped)