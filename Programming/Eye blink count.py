# distance must be 1 meter away
import cv2

# Initialize the Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Blink detection parameters
EYE_CLOSED_FRAMES_THRESHOLD = 3  # Number of frames the eyes must be closed to count as a blink
blink_counter = 0
blink_total = 0
frames_eye_closed = 0

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            # Increment frames where eyes are closed
            frames_eye_closed += 1
        else:
            if frames_eye_closed >= EYE_CLOSED_FRAMES_THRESHOLD:
                # Count a blink if eyes were closed for the threshold number of frames
                blink_total += 1
            # Reset the eye closed frame counter
            frames_eye_closed = 0

        # Draw rectangles around detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the blink count
    cv2.putText(frame, f"Blinks: {blink_total}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Blink Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
