# for more infos about hsv, refer to https://blog.csdn.net/ColdWindHA/article/details/82080176
import cv2
import numpy as np

def empty(p):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow("TrackBars",640,240)


cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# after modification of parameters, get params for image lambo
'''
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",113,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",43,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",58,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
'''


path = "./resources/lambo.jpg"

while True:
    img = cv2.imread(path)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")

    # print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    # pixel with h,s,v in domain [lower,upper) will be mapped to 255/white, otherwise 0/black
    imgMasked = cv2.inRange(imgHSV,lower,upper)
    # use mask to handle the original colorful image
    imgResult = cv2.bitwise_and(img,img,mask=imgMasked)


    # cv2.imshow("original",img)
    # cv2.imshow("hsv",imgHSV)
    # cv2.imshow("mask",imgMasked)
    cv2.imshow("result",imgResult)

    cv2.waitKey(1)