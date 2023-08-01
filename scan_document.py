# scann document
import cv2
import numpy as np

###########################
imgWidth,imgHeight = 640,280
###########################

cap = cv2.VideoCapture(0)
# settings for height, width, brightness ...
cap.set(3,imgWidth)
cap.set(4,imgHeight)
cap.set(10,150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDilation,kernel,iterations=1)

    return imgThres

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    maxArea = 0
    biggest = np.array([])
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # draw contours only if detected area larger than 5000
        if area > 5000:
            # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # calculate the perimeter/zhouchang of the detected area
            perimeter = cv2.arcLength(cnt,True)
            # print(perimeter)
            # approximates a polygonal curve(s) with the specified precision
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)

            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 10)
    return biggest

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)

    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew

def getWarp(img,biggest):
    # print(biggest.shape)
    biggest = reorder(biggest)

    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [imgWidth, 0], [0, imgHeight], [imgWidth, imgHeight]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (imgWidth, imgHeight))

    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(imgWidth,imgHeight))

    return imgCropped

while True:
    _,img = cap.read()
    cv2.resize(img,(imgWidth,imgHeight))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    imgWarpped = getWarp(img,biggest)

    cv2.imshow("Result",imgWarpped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break