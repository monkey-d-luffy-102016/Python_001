import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object
out = cv2.VideoWriter('/home/tejas/Programs/Python/Learn/Opencv-python/output.avi', cv2.VideoWriter_fourcc('X','V','I','D'),20,(frame_width,frame_height))

while True:
    ret,frame = cap.read()

    if not ret:
        print("can't recive frames")
        break

    out.write(frame)

    cv2.imshow("webcam_recording", frame)
     
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
