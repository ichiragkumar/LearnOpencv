import cv2

## load an image from
img =  cv2.imread("assets/RE.jpeg",0)##put mode of image(-1 for transperency, 0 for grey scale mode, 1 fpr including alpha )
## in bgr you get colorfull image


#### resize and rotate this image
#img= cv2.resize(img,(1300,1600))
img= cv2.resize(img,(0,0), fx=2, fy= 2)



###
##rotate this image
#    img =  cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
## 
cv2.imwrite("new.jpeg", img)
 
 
 
# put mode of image(-1 for transperency, 0 for grey scale mode, 1 fpr including alpha )
## in bgr you get colorfull image

cv2.imshow("Roy",img)
cv2.waitKey(0) # wait for 5 seccond

cv2.destroyAllWindows()