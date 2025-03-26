import mediapipe as mp
import cv2

#inintialize mediapipe hand modules
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading")
            break

        #convert BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #detect hands
        results = hands.process(rgb)

        #draw hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        #show the output
        cv2.imshow('Hand Tracking', frame)

        #quit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()