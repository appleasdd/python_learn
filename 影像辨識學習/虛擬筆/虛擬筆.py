import cv2#導入函式cv2
import numpy as np
#讀取影片方式:
#cap = cv2.VideoCapture('aquadance.avi')#將影片導入
#讀取鏡頭方式:
cap = cv2.VideoCapture(0)#0為筆記型電腦專用鏡頭編號
draw1 = []

def findPan(img):
    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    lower = np.array([0,68,11])
    upper = np.array([179,255,255])
    mask = cv2.inRange(hsv,lower,upper)#遮罩製作(過濾顏色)
    result = cv2.bitwise_and(img,img,mask=mask)#過濾回原圖
    penx , peny = findContour(mask)
    cv2.circle(imgcontours,(penx,peny),10,(255,0,0),cv2.FILLED)
    #cv2.bitwise_and(要改變的圖像,要改變的圖像,過濾)
    #將兩個的數值做and的運算並做出遮罩
    cv2.imshow('reslut',result)
    if penx != -1:
        draw1.append([penx,peny,[255,255,255]])
def findContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#找尋輪廓函式
    #contours(輪廓),hierarchy(階層) = cv2.findContours(要偵測的影像,要偵測的輪廓,要使用的近似方法)
    x , y, w,h = -1,-1,-1,-1
    for cnt in contours:
        cv2.drawContours(imgcontours,cnt,-1,(255,0,255),4)
        #cv2.drawContours(要畫的圖片,要畫的輪廓,要畫第幾個輪廓(全部是-1),輪廓的顏色,輪廓的粗細)
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.contourArea(cnt)#算出輪廓的面積
            #cv2.arcLength(cut,True)#算出輪廓邊長
            peri = cv2.arcLength(cnt,True)
            vertices = cv2.approxPolyDP(cnt,peri * 0.02,True)#多邊形近似輪廓
            #vertices = cv2.approxPolyDP(要近似的輪廓,近似值(數值越大多邊形的邊越多),True(封閉圖形)Flase(不封閉圖形))
            x ,y ,w ,h = cv2.boundingRect(vertices) #求多邊形的左上角的x,y座標和寬以及高
    return x+w//2 , y

def dram(draw1):
    for point in draw1:
        cv2.circle(imgcontours,(point[0],point[1]),10,(255,0,0),cv2.FILLED)
while True:
    ret,frame= cap.read()#讀取影響影片前項ret=前一禎(為布林值)frame=後一禎(為布林值) 
    if ret == True:
        imgcontours = frame.copy()
        frame = cv2.resize(frame,(0,0),fx = 1 , fy = 1)#改變影片的大小
        cv2.imshow('video',frame)#秀出圖片(#每個影片皆是用圖片一層一層顯示)
        findPan(frame)
        dram(draw1)
        cv2.imshow('contour',imgcontours)
    if ret == False:
        break#播完就結束
    if  cv2.waitKey(1) == ord('q'):#waitKer(1)為顯示完圖片後所需要等待的毫秒數，數字越大影片速度越慢，ord('q')代表按下此鍵後會直接結束影片
       break