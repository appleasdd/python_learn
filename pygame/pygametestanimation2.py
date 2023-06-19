import pygame
import random
pygame.init()
screen = pygame.display.set_mode((640,320))
pygame.display.set_caption("animation")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))
ball = pygame.Surface((30,30))
pygame.draw.circle(ball,(0,0,255),(15,15),15,0)
rect1 = ball.get_rect()
rect1.center = (320,45)
x, y = rect1.topleft
dx = 3
dy = 3
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += dx
    y += dy
    rect1.center = (x,y)
    if rect1.left <= 0 or rect1.right >= screen.get_width():
        if dx < 0:
            dx = -(random.randint(3,10))
            dx *= -1
        else:
            dx *= -1
    if rect1.top <= 0 or rect1.bottom >= screen.get_height():
        if dy < 0:
            dy = -(random.randint(3,10))
            dy *= -1
        else:
            dy *= -1
    screen.blit(background,(0,0))
    screen.blit(ball, rect1.topleft)
    pygame.display.update()
pygame.quit()