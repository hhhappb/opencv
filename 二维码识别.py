import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode
#img = cv.imread("2.png")
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('data.txt') as f:
    list = f.read().splitlines()
print(list)


while True:
    success,img = cap.read()
    for qrcode in decode(img):
        data = qrcode.data.decode('utf-8')
        print(data)

        if data in list:
            print('ok')
        else :
            print('no')
        pts = np.array([qrcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,(255,0,255),5)
        pts2 = qrcode.rect
        cv.putText(img,data,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
    cv.imshow('w',img)
    cv.waitKey(1)