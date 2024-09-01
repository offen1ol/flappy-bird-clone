import pygame, sys

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird_flap_1 = pygame.image.load('graphics/bird/yellowbird-downflap.png').convert_alpha()
        bird_flap_2 = pygame.image.load('graphics/bird/yellowbird-midflap.png').convert_alpha()
        bird_flap_3 = pygame.image.load('graphics/bird/yellowbird-upflap.png').convert_alpha()
        self.bird_frames = [bird_flap_1,bird_flap_2,bird_flap_3]
        self.bird_index = 0

        self.image = self.bird_frames[self.bird_index]
        self.rect = self.image.get_rect(center = (144,256))
        self.gravity = 0
    
    def animation_state(self):
        self.bird_index += 0.1
        if self.bird_index >= len(self.bird_frames):
            self.bird_index = 0
        self.image = self.bird_frames[int(self.bird_index)]

    def update(self):
        self.animation_state()

# class Base(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('graphics/base.png').convert()
#         self.rect = self.image.get_rect(midbottom = (0,400))

#     def animation_state(self):

pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()
game_active = True

icon = pygame.image.load('graphics/bird/yellowbird-midflap.png').convert_alpha()
pygame.display.set_icon(icon)

bg_surf = pygame.image.load('graphics/background-day.png').convert()
base_surf = pygame.image.load('graphics/base.png').convert()

# Groups
bird = pygame.sprite.GroupSingle()
bird.add(Bird())

# Timer
bird_animation_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bird_animation_timer,900)

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surf,(0,0))
    screen.blit(base_surf,(0,400))

    bird.draw(screen)
    bird.update()

    pygame.display.update()
    clock.tick(60)
