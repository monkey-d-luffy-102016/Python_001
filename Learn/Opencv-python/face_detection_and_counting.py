import cv2

# Load the Haarcascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame")
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Counter for face numbers
    i = 0

    for (x, y, w, h) in faces:
        i += 1  # Increment face number
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)  # Draw rectangle around face
        cv2.putText(frame, f"Face {i}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Label face

    # Display the frame
    cv2.imshow("Face Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
