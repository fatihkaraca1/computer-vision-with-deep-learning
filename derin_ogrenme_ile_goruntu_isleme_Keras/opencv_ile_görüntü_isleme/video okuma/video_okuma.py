import cv2
import time

video_name = "video.mp4"

cap = cv2.VideoCapture(video_name)

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01) #kullanmazsak çok hızlı akar

        cv2.imshow("video",frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

cap.release() #stop capture
cv2.destroyAllWindows()
