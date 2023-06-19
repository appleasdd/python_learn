import pygame
pygame.init()
screen = pygame.display.set_mode((640,320))
pygame.display.set_caption("mumei")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))
pygame.draw.rect(background,(255,255,255),[320,160,25,30],0)
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    pygame.display.update()
pygame.quit()