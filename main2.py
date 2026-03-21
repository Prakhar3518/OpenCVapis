import cv2

myimage2 = cv2.imread('assets/wowpic.jpg',-1)

imagepart = myimage2[100:300,150:400] # new image bnai aur usme purani image ka beech ka part save krlia
myimage2[150:350,250:500] = imagepart # uss part ko orignal image ke andr paste krdia
# jo copy kra aur jo paste krre h uska dimmension same hona chahiye..mtlb 100 - 300 = 150 - 300 same pixels

cv2.imshow('imagemodified',myimage2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(myimage2.shape)

#normally it is RGB but in open CV it is Blue Green Red (BGR)
# all are in the range of 0 - 255 (Where 0 is Nil and 255 is max)