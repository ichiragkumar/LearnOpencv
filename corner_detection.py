import cv2
import numpy as np

img = cv2.imread("assets/chess.png")
img = cv2.resize(img, (0, 0), fx = 0.75, fy = 0.75)## resize the imaage to
img = cv2.resize(img, (1200, 1210))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## now run corner dwttection
#3 parameters are used
## 1. source of image
## 2. number of corners
## 3. minimum Quality
## 4. minimun euclidean distance
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

## display this corneres on screen
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
## search ravel is vey intresting
###### that s it
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size= 3)))## it returns numpy 32 to 64 bits integer value
        cv2.line(img, corner1, corner2, (), 1)



cv2.imshow("Frame Chess", img)
cv2.waitKey(0)
cv2.destroyAllWindows()