import cv2
from deepface import DeepFace

# Access webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Perform emotion detection
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']

        # Display the emotion on the frame
        cv2.putText(frame,
                    f'Dominant Emotion: {dominant_emotion}',
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA)
    except Exception as e:
        print(f"Error: {e}")

    # Display the frame
    cv2.imshow('Webcam - Emotion Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
