import cv2

vehicle = '/home/tejas/Programs/Python/Learn/Opencv-python/cars.xml'

car_cascade = cv2.CascadeClassifier(vehicle)

img = "/home/tejas/Programs/Python/Learn/Opencv-python/cars.png"

img = cv2.imread(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 1, minSize = (30,30) )


for (x,y,w,h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img, "Car", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("Car Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()