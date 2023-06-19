import cv2#導入函式cv2
import numpy as np#導入函式庫numpy
img = np.empty((300,300,3),np.uint8)#產生一個300*300的圖畫，且每一個值為正整數的8bits
for row in range(300):
    for col in range(300):
        img[row][col] = [0,255,0]#每個值等於【0,255,0】
cv2.imshow('img',img)#顯示圖片
cv2.waitKey(0)#顯示時間為永遠