import cv2

vehicle = '/home/tejas/Programs/Python/Learn/Opencv-python/cars.xml'

car_cascade = cv2.CascadeClassifier(vehicle)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors = 1, minSize = (30,30) )

    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Car", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Car Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
