import numpy as np 
import cv2 

# Read the image
img = cv2.imread('/home/tejas/Programs/Python/Learn/Opencv-python/test_corners.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)

if corners is not None:
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)  # Blue circles for corners
else:
    cv2.putText(img, "No corners found", (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
# Show the image
cv2.imshow("Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
