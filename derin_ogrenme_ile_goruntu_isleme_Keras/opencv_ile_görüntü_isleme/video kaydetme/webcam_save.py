import cv2

cap = cv2.VideoCapture(0)

width = int(cv2.CAP_PROP_FRAME_WIDTH)
height = int(cv2.CAP_PROP_FRAME_HEIGHT)
print(width,height)

writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))

while True:
    ret,frame = cap.read()
    cv2.imshow("video",frame)
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()