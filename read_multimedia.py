# read images, videos and webcams
import cv2
print("Package imported!")

# read images
'''
img = cv2.imread("./resources/wyf.jpg")
cv2.imshow("img",img)
cv2.waitKey(0)
'''

# read videos and webcams
# for videos, specify video file path
# for webcams, specify webcam id, 0 for example for integrated webcam of own laptop
cap = cv2.VideoCapture("./resources/memory.mp4")
# settings for height, width, brightness ...
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


