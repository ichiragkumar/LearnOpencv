import cv2
import numpy as np
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
########    a = input("Enter Your Text Display On Your Image")
### kepp displaying the video capture
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))  
       
    
    #########(0,0), (width, height) these are for lines
    ### these are colors and thickness of lines
   ##    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    ##   img = cv2.line(img, (0,height), (width, 0), (0,0,255), 10)## here img become frame 
    ##or you can use frame 
    ### img = cv2.rectangle(img, (100, 100), (200, 200), ( 127, 127, 127), 10)
    ## draw a pop up rectangle on frame of video capture
     ###       img = cv2.circle(img, (300, 300), 60, (0, 0 , 255), -1)
    ### it is making an circle on frame of video
    font = cv2.FONT_HERSHEY_SIMPLEX
   
    img = cv2.putText(frame, "hello chirag", (10, height - 10), font, 10,  (0, 0 , 255), 10, cv2.LINE_AA)
    
    
    cv2.imshow("Frame", img)##or frame 
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()