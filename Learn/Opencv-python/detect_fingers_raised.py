import mediapipe as mp
import cv2

# Initialize mediapipe hand modules
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading")
            break

        # Convert BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands
        results = hands.process(rgb)

        fingers_up = 0
        # Half_raised_fingers = 0  

        
        # Draw hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get hand landmarks
                landmarks = hand_landmarks.landmark

                # Finger tip landmarks (index, middle, ring, pinky)
                finger_tips = [8, 12, 16, 20]
                
                # Thumb tip (compared differently)
                thumb_tip = 4
                
                # half_raised_fingers
                half_fingers = [6,10,14,18]

                #Count half raised thumb(compared differently)
                half_thumb = 3

                # Count fingers raised
                for tip in finger_tips:
                    if landmarks[tip].y < landmarks[tip - 2].y:  # Tip is above lower joint
                        fingers_up += 1

                # Thumb check (compared to palm)
                if landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x:  # Left hand open
                    fingers_up += 1  

                # # Count half raised fingers
                # for half in half_fingers:
                #     if landmarks[half].y < landmarks[half -1].y:
                #         Half_raised_fingers += 1
                
                # # Count half raised thumb
                # if landmarks[half_thumb].y < landmarks[half_thumb - 1].y:
                #         Half_raised_fingers += 1

        # Display the number of fingers up
        cv2.putText(frame, f"Fingers: {fingers_up}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # cv2.putText(frame, f"half_raised_Fingers: {Half_raised_fingers}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the output
        cv2.imshow('Finger Counter', frame)

        # Quit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
