import cv2

myimage = cv2.imread('assets/wowpic.jpg',1)

myimage = cv2.resize(myimage,(640,480)) # to resize a image
myimage = cv2.rotate(myimage, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('editedimage.jpg',myimage) # saves the current image to a folder

cv2.imshow('imagepage',myimage)  # to open image on a page
cv2.waitKey(0)                      # wait for the time to close the image if 0 will not close till i press a key
cv2.destroyAllWindows()