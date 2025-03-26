# OpenCV Cheatsheet

## 1. Getting Started
### Installation
- **Windows:**
  ```bash
  pip install opencv-python
  pip install opencv-contrib-python
  ```
- **Linux:**
  ```bash
  sudo apt update && sudo apt install python3-opencv
  ```
- **Anaconda:**
  ```bash
  conda install -c conda-forge opencv
  ```

## 2. Working with Images
### 2.1 Getting Started
- **Read an Image:**
  ```python
  img = cv2.imread('image.jpg')
  ```
- **Display an Image:**
  ```python
  cv2.imshow('Image', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```
- **Write an Image:**
  ```python
  cv2.imwrite('output.jpg', img)
  ```
- **Convert Color Spaces:**
  ```python
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ```
- **Arithmetic Operations:**
  ```python
  added = cv2.add(img1, img2)
  subtracted = cv2.subtract(img1, img2)
  ```
- **Bitwise Operations:**
  ```python
  bitwise_and = cv2.bitwise_and(img1, img2)
  bitwise_or = cv2.bitwise_or(img1, img2)
  ```

### 2.2 Image Processing
- **Resizing:**
  ```python
  resized = cv2.resize(img, (width, height))
  ```
- **Blurring:**
  ```python
  blurred = cv2.GaussianBlur(img, (5,5), 0)
  ```
- **Edge Detection:**
  ```python
  edges = cv2.Canny(img, 100, 200)
  ```
- **Histogram Equalization:**
  ```python
  equalized = cv2.equalizeHist(gray)
  ```
- **Thresholding:**
  ```python
  _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
  ```
- **Morphological Operations:**
  ```python
  kernel = np.ones((5,5), np.uint8)
  eroded = cv2.erode(img, kernel, iterations=1)
  dilated = cv2.dilate(img, kernel, iterations=1)
  ```

### 2.3 Feature Detection
- **Hough Line Detection:**
  ```python
  lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
  ```
- **Circle Detection:**
  ```python
  circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20)
  ```
- **Corner Detection:**
  ```python
  corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
  ```

### 2.4 Drawing Functions
- **Draw Shapes:**
  ```python
  cv2.line(img, (0, 0), (250, 250), (255, 0, 0), 3)
  cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)
  cv2.circle(img, (150, 150), 50, (0, 0, 255), -1)
  ```
- **Draw Text:**
  ```python
  cv2.putText(img, 'OpenCV', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
  ```

## 3. Working with Videos
### 3.1 Getting Started
- **Play a Video:**
  ```python
  cap = cv2.VideoCapture('video.mp4')
  while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
          break
      cv2.imshow('Video', frame)
      if cv2.waitKey(25) & 0xFF == ord('q'):
          break
  cap.release()
  cv2.destroyAllWindows()
  ```

### 3.2 Video Processing
- **Extract Frames:**
  ```python
  success, image = cap.read()
  count = 0
  while success:
      cv2.imwrite(f"frame{count}.jpg", image)
      success, image = cap.read()
      count += 1
  ```
- **Save Processed Video:**
  ```python
  out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
  out.write(frame)
  out.release()
  ```

## 4. Applications and Projects
- **Face Detection:**
  ```python
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  ```
- **Live Webcam Face Detection:**
  ```python
  cap = cv2.VideoCapture(0)
  while True:
      ret, frame = cap.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.1, 4)
      for (x, y, w, h) in faces:
          cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
      cv2.imshow('Face Detection', frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
  cap.release()
  cv2.destroyAllWindows()
  ```
- **Template Matching:**
  ```python
  result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc
  ```
- **Vehicle Detection:**
  ```python
  car_cascade = cv2.CascadeClassifier('cars.xml')
  cars = car_cascade.detectMultiScale(gray, 1.1, 1)
  ```

---
This cheatsheet provides essential OpenCV functions for quick reference!

