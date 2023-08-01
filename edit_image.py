import cv2
import numpy as np

img = cv2.imread("./resources/wyf.jpg")

# convert colorful image to gray image
imgGary = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# blur/mohu image
imgBlur = cv2.GaussianBlur(imgGary,(7,7),0)

# canny/goule image
# lower threshold for more detailed canny
imgCanny1 = cv2.Canny(img,100,100)
imgCanny2 = cv2.Canny(img,150,200)

# dilate/pengzhang image
# specify the kernel matrix for dilation, a 5x5 identity matrix
kernel = np.ones((5,5),np.uint8)
imgDilation = cv2.dilate(imgCanny1,kernel,iterations=1)

# erode/qinshi image
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

# cv2.imshow("imgGray",imgGary)
# cv2.imshow("imgBlur",imgBlur)
# cv2.imshow("imgCanny1",imgCanny1)
# cv2.imshow("imgCanny2",imgCanny2)
# cv2.imshow("imgDilation",imgDilation)
cv2.imshow("imgEroded",imgEroded)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break