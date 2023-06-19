import cv2
import numpy as np
img = np.zeros((600,600,3),np.uint8)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),1)#畫線
#img.shape[1]==影像的高,img.shape[0]==影像的寬
cv2.rectangle(img,(0,0),(400,300),(0,0,255),cv2.FILLED)
#(img,左上,右下,顏色,邊框粗度(填滿為cv2.FILLED))
cv2.circle(img,(300,400),30,(255,255,255),cv2.FILLED)
#(img,圓心位置,半徑,顏色,粗度(填滿為cv2.FILLED))
cv2.putText(img,'hello',(100,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)
#(img,文字內容,左下座標,字體,大小,顏色,粗度)
cv2.imshow('img',img)
cv2.waitKey(0)
