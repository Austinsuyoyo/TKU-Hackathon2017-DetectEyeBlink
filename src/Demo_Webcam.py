import cv2
import time


cv2.namedWindow('Video')##
video_capture = cv2.VideoCapture(0)
#video_capture.set(3,200)
#video_capture.set(4,100)
# Number of frames to capture
num_frames = 10;

while(video_capture.isOpened()):
 
    ret, frame = video_capture.read()
    
    # Display the resulting frame
    cv2.imshow('Video', frame)
    # Write in csv
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
