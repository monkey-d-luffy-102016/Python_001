


openCV & MediaPipe Cheat Sheet

          1. Basic OpenCV Operations
- `cv2.imread(filename, flag)` – Load an image (`flag`: 0=grayscale, 1=color, -1=unchanged)
- `cv2.imshow(winname, mat)` – Display an image (`winname`: window name, `mat`: image)
- `cv2.imwrite(filename, img)` – Save an image
- `cv2.waitKey(delay)` – Wait for a key event (`delay`: milliseconds)
- `cv2.destroyAllWindows()` – Close all OpenCV windows

----- 2. Video Processing
- `cv2.VideoCapture(source)` – Capture video from camera/file (`source`: 0=webcam, filename=video file)
- `cv2.VideoWriter(filename, fourcc, fps, frameSize)` – Save video (`fourcc`: codec, `fps`: frames per second)

----- 3. Color Space Conversion
- `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` – Convert to grayscale
- `cv2.cvtColor(image, cv2.COLOR_BGR2HSV)` – Convert to HSV
- `cv2.cvtColor(image, cv2.COLOR_BGR2RGB)` – Convert to RGB

----- 4. Drawing Functions
- `cv2.line(image, start, end, color, thickness)` – Draw a line
- `cv2.rectangle(image, pt1, pt2, color, thickness)` – Draw a rectangle
- `cv2.circle(image, center, radius, color, thickness)` – Draw a circle
- `cv2.putText(image, text, org, font, fontScale, color, thickness)` - Draw Text 

----- 5. Image Processing
- `cv2.GaussianBlur(image, (ksize, ksize), sigmaX)` – Apply Gaussian blur (`ksize`: kernel size)
- `cv2.medianBlur(image, ksize)` – Apply median blur
- `cv2.Canny(image, threshold1, threshold2)` – Apply Canny edge detection

----- 6. Morphological Transformations
- `cv2.erode(image, kernel, iterations)` – Erosion
- `cv2.dilate(image, kernel, iterations)` – Dilation
- `cv2.morphologyEx(image, op, kernel)` – Morphological operations

----- 7. Contour Detection
- `cv2.findContours(image, mode, method)` – Find contours
- `cv2.drawContours(image, contours, contourIdx, color, thickness)` – Draw contours

----- 8. Face & Object Detection
- `cv2.CascadeClassifier('path_to_haar_cascade.xml')` – Load a Haar cascade
- `detectMultiScale(image, scaleFactor, minNeighbors, minSize)` – Detect objects

----- 9. Feature Detection
- `cv2.SIFT_create()` – SIFT feature detection
- `cv2.ORB_create()` – ORB feature detection
- `cv2.BFMatcher()` – Brute-Force Matcher

----- 10. Thresholding
- `cv2.threshold(image, thresh, maxval, type)` – Apply threshold
- `cv2.adaptiveThreshold(image, maxValue, adaptiveMethod, thresholdType, blockSize, C)` – Adaptive thresholding

----- 11. Histogram Operations
- `cv2.calcHist([image], channels, mask, histSize, ranges)` – Calculate histogram
- `cv2.equalizeHist(image)` – Histogram equalization

----- 12. Camera Calibration & Perspective Transform
- `cv2.undistort(image, cameraMatrix, distCoeffs)` – Remove distortion
- `cv2.getPerspectiveTransform(pts1, pts2)` – Perspective transform

----- 13. Optical Flow
- `cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, status, err)` – Lucas-Kanade Optical Flow

----- 14. Machine Learning with OpenCV
- `cv2.ml.KNearest_create()` – K-Nearest Neighbors
- `cv2.ml.SVM_create()` – Support Vector Machine
- `cv2.ml.DTrees_create()` – Decision Trees

---

----- MediaPipe Modules
-----# 1. Hands Detection
- `mp.solutions.hands.Hands(min_detection_confidence, min_tracking_confidence)` – Detect hands
- `mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)` – Draw hand landmarks

-----# 2. Face Detection
- `mp.solutions.face_detection.FaceDetection(min_detection_confidence)` – Detect faces
- `face_detection.process(image)` – Process the image for face detection

-----# 3. Pose Estimation
- `mp.solutions.pose.Pose(min_detection_confidence, min_tracking_confidence)` – Detect body pose
- `mp_drawing.draw_landmarks(image, pose_landmarks, mp_pose.POSE_CONNECTIONS)` – Draw body pose landmarks

-----# 4. Holistic Detection (Face, Hands, Pose Together)
- `mp.solutions.holistic.Holistic(min_detection_confidence, min_tracking_confidence)` – Detect multiple body parts

-----# 5. Selfie Segmentation
- `mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=1)` – Segment the background

