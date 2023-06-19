import cv2
from cv2 import HoughLines#導入函式cv2
import numpy as np
#讀取影片方式:
cap = cv2.VideoCapture('德國無限速高速公路-快車道自動讓行.mp4')#將影片導入
#讀取鏡頭方式:
#cap = cv2.VideoCapture(0)#0為筆記型電腦專用鏡頭編號
while True:
    ret,frame= cap.read()#讀取影響影片前項ret=前一禎(為布林值)frame=後一禎(為布林值) 
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        canny = cv2.Canny(blur,50,150)
        height = canny.shape[0]
        width = canny.shape[1]
        mask = np.zeros_like(canny)
        triangle =  np.array([[(200,height),(800,350),(1200,height),]],np.int32)
        cv2.fillPoly(mask, triangle, 255)
        masked_image = cv2.bitwise_and(canny,mask)
        houghLines = cv2.HoughLinesP(masked_image, 2,np.pi/180,100,np.array([]),minLineLength= 40,maxLineGap= 5) 
        line_image = np.zeros_like(frame)
        if houghLines is not None:
            pass
            for line in houghLines:
                x1,y1,x2,y2 = line.reshape(4)
                cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),10)

        cv2.imshow('video',frame)
    if ret == False:
        break#播完就結束
    if  cv2.waitKey(1) == ord('q'):#waitKer(1)為顯示完圖片後所需要等待的毫秒數，數字越大影片速度越慢，ord('q')代表按下此鍵後會直接結束影片
       break
