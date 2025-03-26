import cv2

image = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg")

# gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Gaussian Blur
blur = cv2.GaussianBlur(image, (9,9), 0)

# Canny edge detection 
canny  = cv2.Canny(image, 100, 200)

cv2.imshow("orignal", image)
cv2.imshow("gray", gray_image)
cv2.imshow("Gaussian_Blur", blur)
cv2.imshow("Canny_Edge detection", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()