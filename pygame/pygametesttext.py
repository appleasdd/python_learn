import pygame
pygame.init()
screen = pygame.display.set_mode((640,320))
pygame.display.set_caption("this is my first game")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))
pygame.display.update()
font1 = pygame.font.SysFont("simhei",32)
text = font1.render("Show maker",True,(255,255,255))
background.blit(text,(20,50))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    pygame.display.update()
del font1
pygame.quit()