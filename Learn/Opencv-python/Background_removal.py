import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("can't get frames")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define range of blue colour in HSV
    lower_blue = np.array([100, 150, 50]) # lower range of blue colour for HSV
    upper_blue = np.array([140, 255, 255])# upper range of blue color for HSV

    #thresholf the HSV to get only blue colours
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # invert the masked image to get the backfround
    mask_inv = cv2.bitwise_not(mask)

    # extract result
    result = cv2.bitwise_and(frame, frame, mask=mask_inv)

    #show
    cv2.imshow("original", frame)
    cv2.imshow("background_removed", result)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()