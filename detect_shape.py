# detect shapes and contours/lunkuo
import cv2
import numpy as np

path = "./resources/shapes.jpg"
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

# detect edges in image using canny/goule
imgCanny = cv2.Canny(imgBlur,50,50)

# detect contours
imgContour = img.copy()
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # draw contours only if detected area larger than 500
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            # calculate the perimeter/zhouchang of the detected area
            perimeter = cv2.arcLength(cnt,True)
            # print(perimeter)
            # approximates a polygonal curve(s) with the specified precision
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            # determine the number of edges of a polygon
            objCor = len(approx)
            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                # distinguish between square and rectangle
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor == 5: objectType = "Pentagon"
            else: objectType = "None"
            # draw a bounding box around detected polygons
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            # put info text into the bouding box
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

getContours(imgCanny)

# cv2.imshow("original",img)
# cv2.imshow("gray",imgGray)
# cv2.imshow("blur",imgBlur)
# cv2.imshow("canny",imgCanny)
cv2.imshow("contour",imgContour)
cv2.waitKey(0)