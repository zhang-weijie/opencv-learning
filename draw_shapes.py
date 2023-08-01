import cv2
import numpy as np

# specify matrix for shapes
# img = np.ones((512,512))#black-white channels, zero for black, one for white
img = np.zeros((512,512,3),np.uint8)# bgr channels,

print(img)

# specify zone to be edited and edit it
# img[200:300,100:200] = 255,0,0#convert selected zone from black to blue
# img[:] = 255,0,0 #convert whole image from black to blue, img[:] stands for selection of whole image

# draw a line, from one given point to the other
cv2.line(img,(0,0),(300,300),(0,255,0),12)
# draw a line from a given point to ttom right of the image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)

# draw a rectangle
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),2,cv2.FILLED)# fill selected zone with given color

# draw a circle
cv2.circle(img,(400,50),30,(255,255,0),5)

# put text
cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

cv2.imshow("output",img)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break