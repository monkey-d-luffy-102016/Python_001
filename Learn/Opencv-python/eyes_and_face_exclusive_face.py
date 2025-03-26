import cv2
import numpy as np

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("can't receive frame")
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    eye = eye_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3, minSize= (30,30))

    for (ex,ey,ew,eh) in eye:
        cv2.rectangle(frame, (ex,ey),(ex+ew,ey+eh),(255,0,0),2)

    cv2.imshow("eyes", frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()