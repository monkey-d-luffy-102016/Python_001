import cv2
import numpy as np

image = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg")

#flip the image
horizontally_flipped = np.flip(image, axis = 0)
vertically_flipped = np.flip(image, axis = 1)

#rotate 90
rotate90 = np.rot90(image)

#grayscale conversion
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#display the images
cv2.imshow("Original", image)
cv2.imshow("Horizontally Flipped", horizontally_flipped)
cv2.imshow("Vertically Flipped", vertically_flipped)
cv2.imshow("Rotated 90", rotate90)
cv2.imshow("Grayscale", gray_image)

cv2.waitKey()
cv2.destroyAllWindows()