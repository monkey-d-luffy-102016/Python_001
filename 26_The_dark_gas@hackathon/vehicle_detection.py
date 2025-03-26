import cv2
import time 
start_time = time.time()

traffic = cv2.CascadeClassifier("/home/tejas/Programs/Python/Learn/Opencv-python/cars.xml")

img = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/cars.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = traffic.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 1, minSize = (30,30) )

for (x,y,w,h) in cars:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("detected cars", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
end = time.time()
print("The time of execution of above program is :",
      (end - start_time) * 10**3, "ms")




