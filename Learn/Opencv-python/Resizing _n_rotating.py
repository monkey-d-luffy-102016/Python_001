import cv2

image = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro_gray.jpeg")

#resize the image

resized_image = cv2.resize(image,(300,300))

rotated_image = cv2.rotate(resized_image,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Zoro - Resized", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()