import cv2

img = cv2.imread("shape.jpg")
imgcontours = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img,150,200)
contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#找尋輪廓函式
#contours(輪廓),hierarchy(階層) = cv2.findContours(要偵測的影像,要偵測的輪廓,要使用的近似方法)
for cnt in contours:
    cv2.drawContours(imgcontours,cnt,-1,(255,0,255),4)
    #cv2.drawContours(要畫的圖片,要畫的輪廓,要畫第幾個輪廓(全部是-1),輪廓的顏色,輪廓的粗細)
    area = cv2.contourArea(cnt)
    if area > 500:
        #cv2.contourArea(cnt)#算出輪廓的面積
        #cv2.arcLength(cut,True)#算出輪廓邊長
        peri = cv2.arcLength(cnt,True)
        vertices = cv2.approxPolyDP(cnt,peri * 0.02,True)#多邊形近似輪廓
        corners = len(vertices)#頂點的數量
        #vertices = cv2.approxPolyDP(要近似的輪廓,近似值(數值越大多邊形的邊越多),True(封閉圖形)Flase(不封閉圖形))
        x ,y ,w ,h = cv2.boundingRect(vertices) #求多邊形的左上角的x,y座標和寬以及高
        cv2.rectangle(imgcontours,(x,y),(x+w,y+h),[0,255,0],4)
        if corners == 3:
            cv2.putText(imgcontours,'triangle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],2)
        elif corners == 4:
            cv2.putText(imgcontours,'rectangle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],2)
        elif corners == 5:
            cv2.putText(imgcontours,'pentagon',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],2)
        elif corners >= 6:
            cv2.putText(imgcontours,'circle',(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,0],2)


cv2.imshow("img",img)
cv2.imshow("canny",canny)
cv2.imshow("imgcontours",imgcontours)
cv2.waitKey(0)