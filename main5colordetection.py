import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))


    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #To convert the image color from BGR format to HSV format
    lower_blue = np.array([110, 50, 50])   #Range to select color from
    higher_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, higher_blue)   #it will only show pixels in the given range and black out others

    result = cv2.bitwise_and(frame, frame, mask=mask) # it will only keep the pixels which are common in mask and frame

    cv2.imshow('mask', mask) #will show the selected pixels in white
    cv2.imshow('frame', result) # will show color of the pixels from original frame coz of line 19 logic


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# NO NEED TO DO THESE JUST SIMPLY GO TO A HSV COLOR PICKER AND CHOOSE THE LOWER AND HIGHER RANGE
# BGR_color = np.array([[[255,0,0]]])   #SINGLE PIXEL OF BLUE COLOR
#x = cv2.cvtColor(BGR_color,cv2.COLOR_BGR2HSV) # converted it into HSV color
