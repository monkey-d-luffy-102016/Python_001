import cv2
import cv2.data

cap = cv2.VideoCapture(0)

#loading pretrained model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()

    if not ret:
        print("can't recieve frame")
        break
     # convert to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    # detectMultiScale() detects faces with parameters:
    #  scaleFactor=1.3 → Reduces image size to detect faces at different scales.
    #  minNeighbors=5 → Removes false positives.
    #  minSize=(30, 30) → Ignores very small faces.

    #detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=5,minSize=(30,30))
    
    # Draw rectangles around detected faces
    # here x and y represents start of rectangle
    # here x+w and y+h represnt end of rectangle with dimensions w and h respectively
    # and res tis widht and color
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y+h), (0,255,0),2)
    
    #show the video feed
    cv2.imshow("face detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()