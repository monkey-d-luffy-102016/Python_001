# **TensorFlow with OpenCV Cheatsheet**

## **1. Installing Dependencies**
```bash
pip install tensorflow opencv-python numpy
```

---
## **2. Importing Required Libraries**
```python
import tensorflow as tf
import cv2
import numpy as np
```

---
## **3. Loading a Pre-Trained TensorFlow Model**
```python
model = tf.keras.models.load_model('model.h5')
```

---
## **4. Capturing an Image from Webcam**
```python
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()
cv2.imwrite('captured_image.jpg', frame)
```

---
## **5. Preprocessing Image for Model Input**
```python
image = cv2.imread('captured_image.jpg')
image = cv2.resize(image, (224, 224))
image = image / 255.0  # Normalize pixel values
image = np.expand_dims(image, axis=0)  # Add batch dimension
image = np.array(image, dtype=np.float32)  # Explicit dtype conversion
```

---
## **6. Making Predictions**
```python
predictions = model.predict(image)
print(predictions)
```

---
## **7. Face Detection Using OpenCV & Haarcascades**
```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image_gray = cv2.cvtColor(image[0] * 255, cv2.COLOR_BGR2GRAY).astype(np.uint8)
faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(image[0], (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Face Detection', image[0].astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---
## **8. Object Detection with TensorFlow and OpenCV**
```python
net = cv2.dnn.readNetFromTensorflow('ssd_mobilenet_v2.pb', 'ssd_mobilenet_v2.pbtxt')
blob = cv2.dnn.blobFromImage(image[0] * 255, size=(300, 300), swapRB=True, crop=False)
net.setInput(blob)
output = net.forward()
```

---
## **9. Running TensorFlow Model on a Video Stream**
```python
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    processed_frame = cv2.resize(frame, (224, 224)) / 255.0
    processed_frame = np.expand_dims(processed_frame, axis=0)
    processed_frame = np.array(processed_frame, dtype=np.float32)  # Explicit dtype conversion
    prediction = model.predict(processed_frame)
    
    cv2.imshow('Live Video', (processed_frame[0] * 255).astype(np.uint8))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---
## **10. Saving a Processed Image**
```python
cv2.imwrite('output.jpg', (processed_frame[0] * 255).astype(np.uint8))
```
