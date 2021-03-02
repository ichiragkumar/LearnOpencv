import numpy as np
import cv2
cap = cv2.VideoCapture(0)
### kepp displaying the video capture
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))  
    ## create a blank canvas
    image = np.zeros(frame.shape, np.uint8)## passing shape of my frame)
    smaller_frame  = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    # image[:height//2, :width//2] = smaller_frame ##coping and pasting
    # image[height//2:, :width//2] = smaller_frame
    # image[:height//2, width//2:] = smaller_frame
    # image[height//2:, width//2:] = smaller_frame
    
    
    
    ##rottate this image
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) ##coping and pasting
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame
    
    
    
    
    ## it is created a blank video canvas
    cv2.imshow("Frame", image)##or frame 
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()