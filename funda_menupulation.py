import cv2
import random
## load an image from
img =  cv2.imread("assets/RE.jpeg",-1)##put mode of image(-1 for transperency, 0 for grey 
#scale mode, 1 fpr including alpha )
## in bgr you get colorfull image
##  print(img)## i get numpy array here

#   print(type(img))#########>class numpy.ndarry>

## getting first row of our image
#   print(img[0])



#
#   print(img.shape)#########displaying shapeof a numpy array
### rows - height of image ()
### columns - width of image )()
## channel - color space consist our image in pxl


### first raw of my image
#   print(img[257][45:300])###########

# for i in range(100):
#     for j in range(img.shape[1]):
        
#         img[i][j] = [
#             random.randint(0,255),
#             random.randint(0, 255),
#             random.randint(0, 255)
            
#         ]


## copy part of the images
tag = img[42:150, 57:150]
img[80:90, 50:190] = tag
        
        
        
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()