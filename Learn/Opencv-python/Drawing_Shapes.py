import cv2

image  = cv2.imread("Learn/Opencv-python/Zoro.jpeg")

'''
cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.circle(image, center, radius, color, thickness)
cv2.line(image, start_point, end_point, color, thickness)
cv2.putText(image, text, position, font, size, color, thickness)
'''

# Draw a red rectangle (x=50, y=50) to (x=250, y=250), thickness = 3
cv2.rectangle(image, (50, 50), (250, 250), (0,0,123),3)
# Draw a blue circle at (150, 150) with radius 50, thickness = 2
cv2.circle(image, (150, 150), 50, (255,0,0),2)
# Draw a green line from (50, 300) to (250, 300), thickness = 2
cv2.line(image, (150, 300), (100,350), (0,255,0),2)
# Add text "Zoro" at (100, 400), font size 1, thickness 2
cv2.putText(image, "zoro", (100,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (123,234,200), 2 )

cv2.imshow("Zoro - Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()