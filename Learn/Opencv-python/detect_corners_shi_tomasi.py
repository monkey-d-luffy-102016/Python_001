import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't get frames")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.01, minDistance=10)

    if corners is not None:
        for i in corners:
            x, y = map(int, i.ravel())  # Convert to integers
            cv2.circle(frame, (x, y), 3, (255, 0, 0), 1)

    cv2.imshow("Corners", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
