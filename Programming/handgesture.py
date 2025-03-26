import cv2
import mediapipe as mp
from collections import Counter

# Initialize Mediapipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Indices for fingertip landmarks in Mediapipe
tip_indices = [8, 12, 16, 20]

# Open the webcam
cap = cv2.VideoCapture(0)

def count_fingers(landmarks):
    fingers = []

    # Check thumb (special case, moves differently)
    if landmarks[4].x > landmarks[3].x:  # Right hand thumb comparison (x-axis)
        fingers.append(1)  # Thumb is up
    else:
        fingers.append(0)  # Thumb is down

    # Check other four fingers
    for tip_index in tip_indices:
        # Compare tip y with the knuckle y
        if landmarks[tip_index].y < landmarks[tip_index - 2].y:
            fingers.append(1)  # Finger is up
        else:
            fingers.append(0)  # Finger is down

    # Count fingers up or down
    finger_count = Counter(fingers)
    return finger_count[1], finger_count[0]  # up_count, down_count

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and find hand landmarks
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count fingers
            up_count, down_count = count_fingers(hand_landmarks.landmark)
            print("Fingers up:", up_count)
            print("Fingers down:", down_count)

    # Display the frame
    cv2.imshow("Hand Tracking", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
