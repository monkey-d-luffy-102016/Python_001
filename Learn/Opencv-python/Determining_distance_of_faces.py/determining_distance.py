import cv2
import numpy as np

KNOWN_DISTANCE = 45.0  # Estimated distance of object in cm
KNOWN_WIDTH = 16.4  # Average face width in cm

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Function to calculate focal length
def get_focal_length(measured_distance, real_width, pixel_width):
    return (pixel_width * measured_distance) / real_width

# Function to estimate distance
def estimate_distance(focal_length, real_width, pixel_width):
    return (real_width * focal_length) / pixel_width

# Load reference image
ref_image = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Determining_distance_of_faces.py/ref_image.jpg")
gray = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30,30))

if len(faces) > 0:
    ref_x, ref_y, ref_w, ref_h = faces[0]  # FIXED HERE
    focal_length = get_focal_length(KNOWN_DISTANCE, KNOWN_WIDTH, ref_w)
    print(f"Focal length: {focal_length}")  # FIXED PRINT STATEMENT
else:
    print("No face detected in the reference image.")
    exit()

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame")
        break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))  # FIXED VARIABLE

    for x, y, w, h in faces:
        distance = estimate_distance(focal_length, KNOWN_WIDTH, w)

        # Draw a rectangle (FIXED COORDINATES)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.putText(frame, f"Distance: {int(distance)} cm", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Estimated Distance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
