import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg")

while True:
    ret, frame = cap.read()
    if not ret:
        print("can't reciev frames..")
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    #resize background image

    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))



    #define range of white color in HSV
    lower_white = np.array([0, 0, 0])
    upper_white = np.array([0, 0, 255])

    #mask the image
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # invert the image
    mask_inv = cv2.bitwise_not(mask)

    #bitwise the masked image
    result = cv2.bitwise_and(frame, frame , mask = mask_inv)

    # apply background
    b = cv2.bitwise_and(background, background, mask = mask)

    last_result = cv2.add(result, b)

    # show th output
    cv2.imshow("original", frame)
    cv2.imshow("mask", last_result)
                           
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()