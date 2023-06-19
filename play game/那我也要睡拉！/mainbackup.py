import pygame
import random
import os

#遊戲初始化 ＆ 創建視窗
pygame.init()
pygame.mixer.init()

WIDTH = 500
HIGHT = 600

#creat a window in width * hight
screen = pygame.display.set_mode((WIDTH,HIGHT))

#set title of window
pygame.display.set_caption('My First Pygame')

#set FPS
clock = pygame.time.Clock()
FPS = 60

Fall_speed = 5
score = 0

running = True

#load img
player_img = pygame.image.load('CE94D407-EA75-452A-A211-1E9C4F33064E_1_201_a.jpg').convert()
zzt = pygame.image.load('163885303885437_P7661032.jpg').convert()
#background_img = pygame.image.load(os.path.join('background.JPG')).convert()

#load sound
starting = pygame.mixer.Sound('woo_yeow_swa_lu.wav')
ending = pygame.mixer.Sound('na_woo_yea_yeow_swa_lu.wav')

#load text font
roboto = pygame.font.match_font('Roboto-Thin.ttf')

'''def start_init():
    screen.fill((255,179,179))
    draw_text(screen,'I DONT WANT TO SLEEP!!', 50, WIDTH/2, HIGHT/3)
    pygame.display.update()
    waiting = True
    clock.tick(0)
    while waiting:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                waiting = False
                all_sprite = pygame.sprite.Group()
                #player = Player()
                #all_sprite.add(player)
                player_collition = pygame.sprite.Group()
                #player_collition.add(player)
                rock_collition = pygame.sprite.Group()
                score = 0
                starting.play()
                for i in range(16):
                    r = Rock()
                    all_sprite.add(r)
                    rock_collition.add(r)'''


#shot down & sound play
def shot_down():
    ending.play()
    shot = pygame.mixer.get_busy()
    pygame.time.delay(3000)
    
    return 0
    '''x = 1
    while x:
        if not shot:
            running = False'''
            
# draw score
def draw_text(surf, text, size, x, y ):
    font = pygame.font.Font(roboto, size)
    text_surface = font.render(text, True, (100,100,100))
    text_rext = text_surface.get_rect()
    text_rext.centerx = x
    text_rext.top = y
    surf.blit(text_surface, text_rext)


#creat player
class Player(pygame.sprite.Sprite):

    #初始化player
    def __init__(self):
        #sprite初始化
        pygame.sprite.Sprite.__init__(self)
        #img for player
        self.image = player_img
        #set collition
        self.rect = self.image.get_rect()
        #collition range
        self.radius = 18
        #pygame.draw.circle(self.image, (254,0,0) ,self.rect.center , self.radius )
        #collition width and hight
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HIGHT * 7/8
        #collition move speed
        self.speedx = 8
        starting.play()


    #更新player
    def update(self):

        #detect key press and update sprite(player)
        key_pressed = pygame.key.get_pressed()
        if key_pressed [pygame.K_d] or key_pressed [pygame.K_RIGHT]:
            self.rect.x += self.speedx

        if key_pressed [pygame.K_a] or key_pressed [pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0

        '''self.rect.x += 2
        if self.rect.left > WIDTH:
            self.rect.right = 0'''

#creat rock
class Rock(pygame.sprite.Sprite):


    #初始化rock
    def __init__(self):
        #初始化sprite
        pygame.sprite.Sprite.__init__(self)
        #set img for rock
        self.image = zzt
        #set img color
        #self.image.fill((255,102,255))
        #set collition
        self.rect = self.image.get_rect()
        #set collition
        self.radius = 20
        #spawn rock randomly
        self.rect.centerx =25 + 50 * random.randrange(0,10)
        self.rect.y = 0 - 120 * random.randrange(1,6)
        #fall speed
        self.speedy = Fall_speed

        
    #更新rock
    def update(self):

        #rock fall
        self.rect.y += self.speedy
        
        #replace rock
        if self.rect.top > HIGHT:
            self.rect.centerx = 25 +  50 * random.randrange(0,10)
            self.rect.y = -40
            self.speedy += 0.1

        

all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
player_collition = pygame.sprite.Group()
player_collition.add(player)
rock_collition = pygame.sprite.Group()
for i in range(16):
    r = Rock()
    all_sprite.add(r)
    rock_collition.add(r)


show_init = True
#遊戲迴圈
while(running):

    '''if show_init:
        start_init()
        show_init = False'''

    #FPS per sec
    clock.tick(FPS)

    #input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = shot_down()
            running = False


    #update

    all_sprite.update()
    hits = pygame.sprite.groupcollide(player_collition, rock_collition, False, True,pygame.sprite.collide_circle)
    for hit in hits:
        running = shot_down()
        
        
    score += pygame.time.get_ticks()//1000 - score

    #render
    screen.fill((255,179,179))



    #screen.blit(background_img, (0,0))

    all_sprite.draw(screen)

    draw_text(screen, str(score), 50, WIDTH/2, HIGHT/13)

    pygame.display.update()


pygame.quit()