import cv2#導入函式cv2
import numpy as np
def empty():
    pass
img = cv2.imread('mumei.jpg')
img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)
cv2.namedWindow('Trackbar')#創建視窗和定義名字
cv2.resizeWindow('Trackbar',640,320)#建立視窗的大小
cv2.createTrackbar('HUE MIN','Trackbar',0,179,empty)
cv2.createTrackbar('HUE MAX','Trackbar',179,179,empty)
cv2.createTrackbar('SAT MIN','Trackbar',0,255,empty)
cv2.createTrackbar('SAT MAX','Trackbar',255,255,empty)
cv2.createTrackbar('VAL MIN','Trackbar',0,255,empty)
cv2.createTrackbar('VAL MAX','Trackbar',255,255,empty)
#cv2.createTrackbar(控制條名稱,此控制條的位置,控制條的初始值,控制條的最大值,控制條被改變時所需要動的函式)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#hsv與rgb不同的顏色表示法
#H為色相S為飽和度V為亮度
while True:#獲取各項控制條的變動值
    h_min = cv2.getTrackbarPos('HUE MIN','Trackbar')
    h_max = cv2.getTrackbarPos('HUE MAX','Trackbar')
    s_min = cv2.getTrackbarPos('SAT MIN','Trackbar')
    s_max = cv2.getTrackbarPos('SAT MAX','Trackbar')
    v_min = cv2.getTrackbarPos('VAL MIN','Trackbar')
    v_max = cv2.getTrackbarPos('VAL MAX','Trackbar')
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(hsv,lower,upper)#遮罩製作(過濾顏色)
    result = cv2.bitwise_and(img,img,mask=mask)#過濾回原圖
    #cv2.bitwise_and(要改變的圖像,要改變的圖像,過濾)
    #將兩個的數值做and的運算並做出遮罩
    cv2.imshow('img',img)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    cv2.waitKey(1)


