import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# settings for height, width, brightness ...
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

myColors = [[45,51,91,81,167,255],#green
            [157,73,125,179,255,255]#pink
        ]
# B,G,R
myColorValues = [[51,255,51],
                 [102,102,255]]

# [x,y,colorId]
myPoints = [

]

# detect color
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array([color[0:3]])
        upper = np.array([color[3:6]])
        imgMasked = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(imgMasked)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)

        if x != 0 and y != 0:
            newPoints.append([x,y,count])

        count += 1
        # cv2.imshow(str(color[0]), imgMasked)
    return newPoints

def getContours(img):
    x,y,w,h = 0,0,0,0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # draw contours only if detected area larger than 500
        if area > 500:
            # cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            # calculate the perimeter/zhouchang of the detected area
            perimeter = cv2.arcLength(cnt,True)
            # print(perimeter)
            # approximates a polygonal curve(s) with the specified precision
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)

while True:
    _,img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)

    if len(newPoints) != 0:
        for point in newPoints:
            myPoints.append(point)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break