import cv2

def click_event(event, x, y, flags, parameters):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, str(x) + ',' + str(y),(x,y), font, 1, (255,0,0), 2)
        cv2.imshow('Image', img)


    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (x-50, y-50), (x+50, y+50), (0, 255, 0), 2)
        cv2.imshow('Image', img)

        font = cv2.FONT_HERSHEY_COMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        cv2.putText(img, str(b) + ',' + str(g), (x,y), font, 1,(255,255,0), 2 )

if __name__ == "__main__":

    img = cv2.imread("/home/tejas/Programs/Python/Learn/Opencv-python/Zoro.jpeg")

    cv2.imshow('Image', img)

    cv2.setMouseCallback('Image', click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
