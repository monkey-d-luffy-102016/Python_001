import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("can't recieve frames..")
        break
    # hue saturation value(HSV) is a color model that describes colors in terms of their hue, saturation and value
    #Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #define ranges of red color in HSV
    # Hue (H) → Represents the color (0-179 in OpenCV, 0°-360° in standard HSV).
    # Saturation (S) → Intensity of the color (0-255).
    # Value (V) → Brightness of the color (0-255).

    lower_blue = np.array([100, 150, 50]) # lower range of blue colour for HSV
    upper_blue = np.array([140, 255, 255])# upper range of blue color for HSV

    # Create mask to filter only red objects
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("original", frame)
    cv2.imshow("result", result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
