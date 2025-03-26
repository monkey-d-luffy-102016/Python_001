import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Set up blob detector parameters
parameters = cv2.SimpleBlobDetector_Params()

parameters.filterByArea = True
parameters.minArea = 100

parameters.filterByCircularity = True
parameters.minCircularity = 0.5

parameters.filterByConvexity = True
parameters.minConvexity = 0.8

parameters.filterByInertia = True
parameters.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(parameters)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't get frames")
        break

    keypoints = detector.detect(frame)

    # Draw blobs on the image as red circles
    blank = np.zeros((1, 1), dtype=np.uint8)
    blobs = cv2.drawKeypoints(frame, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)
    text = f"Number of Circular Blobs: {number_of_blobs}"

    cv2.putText(blobs, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Blob Detection", blobs)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
