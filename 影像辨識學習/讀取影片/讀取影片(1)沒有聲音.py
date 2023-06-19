import cv2#導入函式cv2
#讀取影片方式:
#cap = cv2.VideoCapture('aquadance.avi')#將影片導入
#讀取鏡頭方式:
cap = cv2.VideoCapture(0)#0為筆記型電腦專用鏡頭編號
while True:
    ret,frame= cap.read()#讀取影響影片前項ret=前一禎(為布林值)frame=後一禎(為布林值) 
    if ret == True:
        frame = cv2.resize(frame,(0,0),fx = 0.5 , fy = 0.5)#改變影片的大小
        cv2.imshow('video',frame)#秀出圖片(#每個影片皆是用圖片一層一層顯示)
    if ret == False:
        break#播完就結束
    if  cv2.waitKey(1) == ord('q'):#waitKer(1)為顯示完圖片後所需要等待的毫秒數，數字越大影片速度越慢，ord('q')代表按下此鍵後會直接結束影片
       break

