"""
軟體系一年級
唐知謙
學號:411077018
遊戲規則:
w:向上
S:向下
如果碰到左邊視窗邊邊就結束遊戲
並會顯示你最後的積分
"""
import pygame #導入函式庫pygame
import random #導入函式庫random
pygame.init() #初始化pygame
screen = pygame.display.set_mode((1000,600)) #建立視窗
pygame.display.set_caption("this is my first game") #顯示標題
background = pygame.Surface(screen.get_size()) #建立畫布
background = background.convert() #可以加快顯示速度
background.fill((0,0,0)) #建立畫布顏色
cube = pygame.Surface((10,150)) #建立方塊畫布
ball = pygame.Surface((30,30)) #建立圓形畫布
pygame.draw.rect(cube,(255,255,255),[0,0,10,150],0) #畫出方塊
pygame.draw.circle(ball,(0,0,255),(15,15),15,0) #建立圓形
rect1 = ball.get_rect() #取得圓形區塊
rect1.center = (320,45) #球起始中心位置
rect2 = cube.get_rect() #取得方塊區塊
rect2.center = (20,160) #方塊起始位置
a = int() #記分變數
x, y = rect1.topleft #球初始在座上角座標
x1, y1 = rect2.topleft #方塊初始在座上角座標
dx = 6 #球的x初始速度
dy = 6 #球的y初始速度
ay = 45 #方塊y的移動變數
clock = pygame.time.Clock() #計時物件
running = True #使遊戲無限運作
while running: #使遊戲無限運作
    clock.tick(60) #以60禎的速度運行程式
    for event in pygame.event.get(): #確認是否獲取滑鼠按鍵
        if event.type == pygame.QUIT: #確認是否按下關閉鍵
            running = False  #結束遊戲
            print("Thank you play this game") #印出Thank you play this game
        elif event.type == pygame.KEYDOWN: #確認是否獲取鍵盤按鍵
            if event.key == pygame.K_w: #如果按下w鍵
                y1 -= ay #(方塊)y1減ay變數
            elif event.key == pygame.K_s: #如果按下s鍵
                y1 += ay #(方塊)y1加ay變數
    if rect2.top <= 0: #如果方塊會跑出上邊視窗
        y1 += 80 # 方塊(y1)加80
    if rect2.bottom >= screen.get_height(): #如果方塊會跑出下邊視窗
        y1 -= 80 #方塊(y2)加80
    rect2.center = (x1,y1) #改變方塊位置
    x += dx #球的x加上dx變數
    y += dy #球的y加上dy變數
    rect1.center = (x,y) #改變球的位置
    if rect1.left <= rect2.right and rect2.bottom >= rect1.top >= rect2.top: #如果球撞到方塊
        if dx < 0: #如果dx小於0
            dx = -(random.randint(4,6)) #隨機改變dx數值(範圍4到6)
            dx *= -1 #使球反彈
        else: #如果dx大於0
            dx *= -1 #使球反彈
        a += 1 #撞到方塊後加一分
        print(a) #印出a
    if rect1.right >= screen.get_width(): #如果球撞到視窗右邊
        if dx < 0: #如果dx小於0
            dx = -(random.randint(4,6)) #隨機改變dx數值(範圍4到6)
            dx *= -1 #使球反彈
        else: #如果dx大於0
            dx *= -1 #使球反彈
    if rect1.top <= 0 or rect1.bottom >= screen.get_height(): #如果球撞到視窗上下邊
        if dy < 0: #如果dy小於0
            dy = -(random.randint(4,6)) #隨機改變dy數值(範圍4到6)
            dy *= -1 #使球反彈
        else: #如果dy大於0
            dy *= -1 #使球反彈
    screen.blit(background,(0,0)) #在繪圖視窗加上畫布
    screen.blit(ball, rect1.topleft) #在繪圖視窗繪製球
    screen.blit(cube, rect2.topleft) #在繪圖視窗繪製方塊
    pygame.display.update() #更新視窗
    if  rect1.left <= 0: #如果球撞上左邊
        running = False #結束遊戲
        pygame.quit() #關閉視窗
        print("Thank you play this game") #印出Thank you play this game
        print("you collide %d" %a) #印出得分
pygame.quit() #關閉視窗