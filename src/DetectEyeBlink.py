import cv2
import sys
import numpy as np
from datetime import datetime
import time


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade  = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
file = open('./data11.csv', 'a')##CSV
format = "%H:%M:%S"##CSV
cv2.namedWindow('Video')##
#cv2.moveWindow('Video',870,460)
video_capture = cv2.VideoCapture(0)
video_capture.set(3,300)
video_capture.set(4,280)
eye_count=[]
SecondCnt=0
eye_count = 0
while(video_capture.isOpened()):
    detect = 1
    # FPS start time
    start = time.time()
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ~detect:
        if(eye_count>4):
            print("WAKEUPPPPP")

    eyes = eyeCascade.detectMultiScale(gray,1.1,5)

    if(len(eyes)==0):
        eye_count+=1
        detect = 0
    if len(eyes)==2 or len(eyes)==1 :
        eye_count=0        
        detect = 1
    for(ex, ey, ew, eh)in eyes:
        #print eyes
        date = datetime.now().strftime(format)##CSV
        file.write(date+',1')##CSV
        file.write("\n")##CSV
        cv2.rectangle(frame,(ex, ey), (ex+ew, ey+eh), (100, 255, 255), 2)
    # Fps end time and show
    end = time.time()
    FPS = 1/(end-start)
    cv2.putText(frame,'{:02.3f}'.format(FPS),(0,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    # Write in csv
    date = datetime.now().strftime(format)
    file.write(date+',0')
    file.write("\n")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
 
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
