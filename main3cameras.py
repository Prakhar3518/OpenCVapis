import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Create a VideoCapture object to access the webcam
# 0 = default webcam (use 1, 2... if multiple cameras are connected)

while True:
    # Infinite loop to continuously capture video frames

    ret, frame = cap.read()
    # cap.read() captures a frame from the webcam
    # ret = True/False (whether frame was captured successfully)
    # frame = the actual image (each frame of the video)

    cv2.imshow('frame', frame)
    # Display the frame in a window named 'frame'

    if cv2.waitKey(1) == ord('q'):
        # waitKey(1) waits 1 millisecond for a key press
        # ord('q') converts 'q' into its ASCII value
        # If 'q' is pressed → exit the loop
        break

cap.release()
# Release the webcam (important so other apps can use it later)

cv2.destroyAllWindows()
# Close all OpenCV windows that were opened