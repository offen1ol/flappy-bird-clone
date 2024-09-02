import pygame, sys

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird_flap_1 = pygame.image.load('graphics/bird/yellowbird-midflap.png').convert_alpha()
        bird_flap_2 = pygame.image.load('graphics/bird/yellowbird-upflap.png').convert_alpha()
        bird_flap_3 = pygame.image.load('graphics/bird/yellowbird-downflap.png').convert_alpha()
        self.bird_frames = [bird_flap_1,bird_flap_2,bird_flap_3]
        self.bird_index = 0

        self.image = self.bird_frames[self.bird_index]
        self.rect = self.image.get_rect(center = (144,256))
        self.gravity = 0
        self.height_marker = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()

        self.image = pygame.transform.rotate(self.image, -90)

        if keys[pygame.K_SPACE]:
            self.gravity = -4
            self.image = pygame.transform.rotate(self.image, 120)
            self.height_marker = self.rect.bottom

        if self.rect.bottom < self.height_marker:
            self.image = pygame.transform.rotate(self.image, 90)

    def animation_state(self):
        if self.rect.bottom == 400:
            self.image = self.bird_frames[0]
        else:
            self.bird_index += 0.1
            if self.bird_index >= len(self.bird_frames):
                self.bird_index = 0
            self.image = self.bird_frames[int(self.bird_index)]
    
    def apply_gravity(self):
        self.gravity += 0.25
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400

    def update(self):
        self.animation_state()
        self.player_input()
        self.apply_gravity()

# def collision_check():
#     if pygame.Rect.colliderect(bird.sprite, )

pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()
game_active = False

icon = pygame.image.load('graphics/bird/yellowbird-midflap.png').convert_alpha()
pygame.display.set_icon(icon)

bg_surf = pygame.image.load('graphics/background-day.png').convert()
base_surf = pygame.image.load('graphics/base.png').convert()
base_width = 288
base_i = 0

# Groups
bird = pygame.sprite.GroupSingle()
bird.add(Bird())

# Timer
bird_animation_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bird_animation_timer,1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if game_active:
            
        # else:
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
    
    screen.blit(bg_surf,(0,0))

    # Loop base_surf forever
    screen.blit(base_surf,(base_i,400))
    screen.blit(base_surf,(base_width+base_i,400))
    if base_i == -base_width:
        screen.blit(base_surf,(base_width+base_i,400))
        base_i = 0
    base_i -= 1

    if game_active:
        bird.draw(screen)
        bird.update()
    
    else:
        bird.draw(screen)

    pygame.display.update()
    clock.tick(60)
