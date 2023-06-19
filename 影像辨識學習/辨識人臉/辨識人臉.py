import cv2#導入函式cv2
#img = cv2.imread('lenna.jpg')
cap = cv2.VideoCapture(0)
while True:
    ret,frame= cap.read()
    if ret == True:
        faceCascade = cv2.CascadeClassifier('face_detect.xml')#載入學習器
        frame = cv2.resize(frame,(0,0),fx = 1 , fy = 1)#改變影片的大小
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faceRect = faceCascade.detectMultiScale(gray,2.4,1)
    #faceCascade.detectMultiScale(要檢測的影像,縮小倍率,需要框的次數(數字越大越嚴謹))
        for (x,y,w,h) in faceRect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if ret == False:
            break#播完就結束
        if  cv2.waitKey(1) == ord('q'):#waitKer(1)為顯示完圖片後所需要等待的毫秒數，數字越大影片速度越慢，ord('q')代表按下此鍵後會直接結束影片
            break
        cv2.imshow('video',frame)