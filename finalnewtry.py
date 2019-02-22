import cv2
import time
import numpy as np
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    fc=cv2.CascadeClassifier('C:\\Project\\DevSoc19\\haarcascade_frontalface_default.xml')
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
#    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    Error in recognizing!!
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        continue
    try:
        faces=fc.detectMultiScale(gray)
        #cv2.imshow('Original',frame)
        #print("Type => ",type(faces),"\nFaces =>",faces,"\nShape =>",faces.shape)
    #  ERRORRRRRRR!!!!!!!!!!!!!!!!!  --- Need to resolve L8R
        print("Population Density => ",str(faces.shape[0]))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,100,0),1)
        cv2.rectangle(frame,((0,frame.shape[0]-25)),(270, frame.shape[0]), (255,255,255), -1)
        cv2.putText(frame, "Number of people: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_ITALIC, 0.5, (0,0,0), 1)
        cv2.imshow('Density',frame)
    except AttributeError:
        print("No person in scope!!!")
        continue
    #cv2.waitkey(3000)
    #time.sleep(1)          Too much laggy --Need 2 remove L8R
    finally:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
