import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    fc=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
#    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        continue
    faces=fc.detectMultiScale(gray)
    print("Type => ",type(faces),"\nFaces =>",faces,"\nShape =>",faces.shape)
#  ERRORRRRRRR!!!!!!!!!!!!!!!!!
    print("\n\n Number of people => ",str(faces.shape[0]))
# ERRORRRRRRR!!!!!!!!!!!!!!!!!!
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,100,0),1)
    cv2.rectangle(frame,((0,frame.shape[0]-25)),(270, frame.shape[0]), (255,255,255), -1)
    cv2.putText(frame, "Number of people: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0), 1)
    cv2.imshow('Density',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
