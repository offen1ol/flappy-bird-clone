import pygame, sys

pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()

icon = pygame.image.load('graphics/bird/yellowbird-midflap.png').convert_alpha()
pygame.display.set_icon(icon)

bg_surf = pygame.image.load('graphics/background-day.png').convert()
base_surf = pygame.image.load('graphics/base.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surf,(0,0))
    screen.blit(base_surf,(0,400))


    pygame.display.update()
    clock.tick(60)
