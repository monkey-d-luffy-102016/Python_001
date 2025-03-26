import cv2
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# Load the object detection model from TensorFlow Hub
model = hub.load('https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2')

# Load the labels for the COCO dataset
labels = {1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane',
          6: 'bus', 7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light',
          11: 'fire hydrant', 13: 'stop sign', 14: 'parking meter', 15: 'bench',
          16: 'bird', 17: 'cat', 18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow',
          22: 'elephant', 23: 'bear', 24: 'zebra', 25: 'giraffe', 27: 'backpack',
          28: 'umbrella', 31: 'handbag', 32: 'tie', 33: 'suitcase', 34: 'frisbee',
          35: 'skis', 36: 'snowboard', 37: 'sports ball', 38: 'kite', 39: 'baseball bat',
          40: 'baseball glove', 41: 'skateboard', 42: 'surfboard', 43: 'tennis racket',
          44: 'bottle', 46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife',
          50: 'spoon', 51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich',
          55: 'orange', 56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza',
          60: 'donut', 61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant',
          65: 'bed', 67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop',
          74: 'mouse', 75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave',
          79: 'oven', 80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book',
          85: 'clock', 86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier',
          90: 'toothbrush'}

# Initialize the webcam
cap = cv2.VideoCapture(0)

frame_number = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize the image to 300x300
    image_resized = tf.image.resize(image_rgb, (300, 300))

    # Convert the image to uint8
    image_uint8 = tf.cast(image_resized, dtype=tf.uint8)

    # Add a batch dimension
    input_tensor = tf.convert_to_tensor(image_uint8)
    input_tensor = input_tensor[tf.newaxis, ...]

    # Perform object detection
    detections = model(input_tensor)

    # Extract detection results
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}

    boxes = detections['detection_boxes']
    classes = detections['detection_classes'].astype(int)
    scores = detections['detection_scores']

    # Visualize detection results
    height, width, _ = frame.shape
    for i in range(len(boxes)):
        if scores[i] >= 0.5:  # Display only detections with confidence >= 0.5
            ymin, xmin, ymax, xmax = boxes[i]
            left, right, top, bottom = int(xmin * width), int(xmax * width), int(ymin * height), int(ymax * height)

            # Draw bounding box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Display label
            label = f"{labels.get(classes[i], 'Unknown')} {scores[i]:.2f}"
            cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Save the frame to disk
    cv2.imwrite(f"output_frame_{frame_number}.jpg", frame)
    frame_number += 1

    # Stop after saving a certain number of frames (optional)
    if frame_number > 100:  # Save 100 frames, adjust as needed
        break

# When everything is done, release the capture
cap.release()
