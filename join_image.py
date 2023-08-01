import cv2
import numpy as np

img = cv2.imread("./resources/wyf.jpg")

# join images horizontally
joinedHorizontal = np.hstack((img,img))
# join images vertically
joinedVertical = np.vstack((img,img))

cv2.imshow("Horizontal",joinedHorizontal)
cv2.imshow("Vertical",joinedVertical)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break