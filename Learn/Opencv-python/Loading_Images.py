import cv2

image = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg")

cv2.imshow("zoro", image)
cv2.waitKey(0)
cv2.destroyAllWindows()