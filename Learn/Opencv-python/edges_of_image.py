import cv2 
  
# Reads the image 
img = cv2.imread('Learn/Opencv-python/Zoro.jpeg') 
  
# Applying Laplacian filter
laplacian = cv2.Laplacian(img, cv2.CV_64F) 
cv2.imshow('EdgeMap', laplacian)  
  
cv2.waitKey(0)          
cv2.destroyAllWindows() 