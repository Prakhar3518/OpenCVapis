import numpy as np
import cv2

myimage = cv2.imread('assets/carr.jpg')

myimage = cv2.resize(myimage,(0,0), fx=0.25, fy=0.25)
grayimage = cv2.cvtColor(myimage, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grayimage, 200, 0.01, 5)
corners = corners.astype(int)  #By default, goodfreaturestotrack gives corners in float so this changes it into int

for i in corners:
    x, y = i.ravel()  #now the points are in matrix like [[[100,112]]]....ravel removes the brackets and returns the value so x = 100 and y = 112
    cv2.circle(myimage, (x, y), 5, 255, -1)

cv2.imshow('carr', myimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
