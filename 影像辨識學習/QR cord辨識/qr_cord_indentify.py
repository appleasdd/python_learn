import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import webbrowser

cap = cv2.VideoCapture(0) #開啟鏡頭

qrcode = cv2.QRCodeDetector()
def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)   # 轉置矩陣，把 x 放在同一欄，y 放在同一欄
    xmax = int(np.amax(box_roll[0]))  # 取出 x 最大值
    xmin = int(np.amin(box_roll[0]))  # 取出 x 最小值
    ymax = int(np.amax(box_roll[1]))  # 取出 y 最大值
    ymin = int(np.amin(box_roll[1]))  # 取出 y 最小值
    return (xmin,ymin,xmax,ymax)
while True:
    ret, frame = cap.read()
    data, bbox, rectified = qrcode.detectAndDecode(frame)
    print(bool(data))
    if bbox is not None:
        """
        print(data)                # QRCode 的內容
        print(bbox)                # QRCode 的邊界
        print(rectified)           # 換成垂直 90 度的陣列
        """
        box = boxSize(bbox[0])
        cv2.rectangle(frame,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)
        if bool(data) == True:
            print(data)
            url = data
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new(url)
            break
    cv2.imshow('video',frame)
    if ret == False or cv2.waitKey(20) == ord('q'):
        break