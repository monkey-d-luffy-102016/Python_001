import cv2

# open webcam 0 for default video bus
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read() # assigns ret and frame

    if not ret:
        print("can't recieve frame")
        break

    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()