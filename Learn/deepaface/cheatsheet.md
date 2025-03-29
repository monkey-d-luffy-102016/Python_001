# DeepFace Cheatsheet

## 1. Installation
```bash
pip install deepface
```

## 2. Face Verification
```python
from deepface import DeepFace

result = DeepFace.verify(img1_path="face1.jpg", img2_path="face2.jpg")
print(result)
```

## 3. Face Recognition (Find Similar Faces in Database)
```python
DeepFace.find(img_path="unknown.jpg", db_path="/path/to/database")
```

## 4. Face Analysis (Age, Gender, Emotion, Race)
```python
analysis = DeepFace.analyze(img_path="face.jpg", actions=['age', 'gender', 'emotion', 'race'])
print(analysis)
```

## 5. Model Selection
```python
DeepFace.verify(img1_path, img2_path, model_name="Facenet")
```
- Supported Models: `VGG-Face`, `Google-FaceNet`, `OpenFace`, `DeepID`, `Dlib`, `ArcFace`

## 6. Using OpenCV for Face Detection
```python
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

## 7. Real-Time Face Recognition with DeepFace
```python
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        cv2.imwrite("temp.jpg", face)
        result = DeepFace.find(img_path="temp.jpg", db_path="images/")
        if len(result) > 0:
            name = result[0]['identity'][0].split("/")[-1]
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

## 8. Training Custom Face Recognition Model (TensorFlow)
```python
import tensorflow as tf
import numpy as np
import cv2
import os

# Load images
data_dir = "images/"
classes = os.listdir(data_dir)
X, y = [], []

for label, person in enumerate(classes):
    person_dir = os.path.join(data_dir, person)
    for img_name in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (128, 128))
        X.append(img)
        y.append(label)

X = np.array(X) / 255.0
y = tf.keras.utils.to_categorical(np.array(y), num_classes=len(classes))

# Define CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(classes), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=16, validation_split=0.2)

# Save the model
model.save("face_recognition_model.h5")
```

## 9. Using the Trained Model for Real-Time Recognition
```python
model = tf.keras.models.load_model("face_recognition_model.h5")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (128, 128))
        face = np.expand_dims(face, axis=0) / 255.0
        
        prediction = model.predict(face)
        class_index = np.argmax(prediction)
        name = classes[class_index]
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

## Summary
- `DeepFace.verify()` → Compare two faces.
- `DeepFace.find()` → Identify a face from a database.
- `DeepFace.analyze()` → Get emotions, age, gender, and race.
- `OpenCV` → Use Haar cascades for real-time face detection.
- `TensorFlow` → Train and use a custom CNN model for face recognition.

This cheatsheet covers everything you need for DeepFace and face recognition! 🚀
