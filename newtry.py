import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',hsv)
    cap.get(3)
    cap.get(4)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
