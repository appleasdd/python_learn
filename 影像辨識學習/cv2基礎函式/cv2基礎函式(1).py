from email import iterators
import cv2#導入函式cv2
import numpy as np#導入函式庫numpy
import random
img = cv2.imread("mumei.jpg")
img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#使圖片黑白化
blur = cv2.GaussianBlur(img,(9,9),0)#使影像高斯模糊(數字只能奇數)最後數字為標準差
canny = cv2.Canny(img,100,200)#邊緣化(前數為最低值,後數為最高值)
kernerl = np.ones((3,3),np.uint8)#配合dilate(數字越大邊緣越粗)
dilate = cv2.dilate(canny,kernerl,iterations=1)#邊緣加粗化(盡量配合以邊緣化影像)
kerner2 = kernerl = np.ones((4,4),np.uint8)#配合erode(數字越大邊緣越細)
erode = cv2.erode(dilate,kerner2,iterations=1)#邊緣細化(盡量配合以邊緣化影像)
cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)