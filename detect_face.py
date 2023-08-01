''' available models
haarcascade_eye_tree_eyeglasses.xml      haarcascade_lefteye_2splits.xml
haarcascade_eye.xml                      haarcascade_licence_plate_rus_16stages.xml
haarcascade_frontalcatface_extended.xml  haarcascade_lowerbody.xml
haarcascade_frontalcatface.xml           haarcascade_profileface.xml
haarcascade_frontalface_alt2.xml         haarcascade_righteye_2splits.xml
haarcascade_frontalface_alt_tree.xml     haarcascade_russian_plate_number.xml
haarcascade_frontalface_alt.xml          haarcascade_smile.xml
haarcascade_frontalface_default.xml      haarcascade_upperbody.xml
haarcascade_fullbody.xml
'''
import cv2

modelDir = "/root/anaconda3/pkgs/libopencv-4.5.5-py39h7d09d5f_0/share/opencv4/haarcascades/"
faceCascade = cv2.CascadeClassifier(modelDir + "haarcascade_righteye_2splits.xml")

img = cv2.imread("./resources/wyf.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("result",img)
cv2.waitKey(0)