import cv2
import numpy as np
import tensorflow as tf

# Load pre-trained mask detection model
model = tf.keras.models.load_model("/home/tejas/Downloads/model.h5")

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcamq
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    
    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (224, 224))  # Resize for model
        face_img = np.expand_dims(face_img, axis=0) / 255.0  # Normalize
        
        # Predict mask/no mask
        prediction = model.predict(face_img)[0][0]
        
        if prediction < 0.5:
            label = "Mask"
            color = (0, 255, 0)
        else:
            label = "No Mask"
            color = (0, 0, 255)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    cv2.imshow("Face Mask Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
