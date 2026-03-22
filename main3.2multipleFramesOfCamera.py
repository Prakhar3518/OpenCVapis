import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # cap.get is a property and 3 is used for width and 4 is used for height they are 15 other properties as well
    height = int(cap.get(4))


    smaller_frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)

    image = np.zeros(frame.shape, np.uint8) # new empty pic , frame.shape to make it of same size,np.uint is for unsigned datatype

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    cv2.imshow('imagepage',image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
