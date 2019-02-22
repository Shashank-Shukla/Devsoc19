import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[100:900, 100:900]
    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',hsv)
    cap.get(3)
    cap.get(4)
    lower_lim = np.array([0,20,70], dtype=np.uint8)
    upper_lim = np.array([20,255,255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_lim, upper_lim)
    mask = cv2.dilate(mask,kernel,iterations = 4)
    mask = cv2.GaussianBlur(mask,(5,5),100)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
    #cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
