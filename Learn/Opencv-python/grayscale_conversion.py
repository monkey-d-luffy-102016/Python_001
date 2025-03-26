import cv2

image = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro_gray.jpeg", gray_image)

#display the grayscale image

cv2.imshow("Zoro - Grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()