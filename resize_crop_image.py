import cv2

img = cv2.imread("./resources/wyf.jpg")
print(img.shape)

# change width and height of given image
imgResized = cv2.resize(img,(1000,1000))

# crop/caijian image according to specified height and width
imgCropped = img[0:200,200:500]


# cv2.imshow("Original image",img)
# cv2.imshow("imgResized",imgResized)
cv2.imshow("imgCropped",imgCropped)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break