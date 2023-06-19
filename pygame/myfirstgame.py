import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("this is my first game")
pygame.mixer.init()
pygame.mixer.music.load("Produce (online-audio-converter.com).ogg")
pygame.mixer.music.play(-1)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))
cube = pygame.Surface((10,150))
ball = pygame.Surface((30,30))
pygame.draw.rect(cube,(255,255,255),[0,0,10,150],0)
pygame.draw.circle(ball,(0,0,255),(15,15),15,0)
rect1 = ball.get_rect()
rect1.center = (320,45)
rect2 = cube.get_rect()
rect2.center = (20,160)
a = int()
x, y = rect1.topleft
x1, y1 = rect2.topleft
dx = 6
dy = 6
ay = 30
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Thank you play this game")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1 -= ay
            elif event.key == pygame.K_s:
                y1 += ay
    if rect2.top <= 0:
        y1 += 80
    if rect2.bottom >= screen.get_height():
        y1 -= 80
    rect2.center = (x1,y1)
    x += dx
    y += dy
    rect1.center = (x,y)
    if rect1.left <= rect2.right and rect2.bottom >= rect1.top >= rect2.top:
        if dx < 0:
            dx = -(random.randint(4,6))
            dx *= -1
        else:
            dx *= -1
        a += 1
        print(a)
    if rect1.right >= screen.get_width():
        if dx < 0:
            dx = -(random.randint(4,6))
            dx *= -1
        else:
            dx *= -1
    if rect1.top <= 0 or rect1.bottom >= screen.get_height():
        if dy < 0:
            dy = -(random.randint(4,6))
            dy *= -1
        else:
            dy *= -1
    screen.blit(background,(0,0))
    screen.blit(ball, rect1.topleft)
    screen.blit(cube, rect2.topleft) 
    pygame.display.update()
    if  rect1.left <= 0:
        running = False
        pygame.quit()
        print("Thank you play this game")
        print("you collide %d" %a)
pygame.quit()