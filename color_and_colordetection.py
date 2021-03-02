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
## different ways to understanding color
        #   ----> RGB
        #   ----> BGR
        #   ----> HSV hue saturation and brightness / litness /
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) ### it takes hsv color on screen
    ##need lower bound and upeer bound to
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
        
    mask = cv2.inRange(hsv, lower_blue, upper_blue)### black and white color screen
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("Frame", result)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()