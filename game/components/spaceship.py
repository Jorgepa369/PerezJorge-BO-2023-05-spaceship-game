import pygame
from pygame.sprite import Sprite

from game.utils.constants import SOUND_SHOOT, SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_POS_X = (SCREEN_WIDTH // 2) - SPACESHIP_HEIGHT
    SPACESHIP_POS_Y = 500
    SPACESHIP_SPEED = 10    

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.SPACESHIP_POS_X
        self.rect.y = self.SPACESHIP_POS_Y        
        self.type = 'player'
        self.has_power_up = False
        self.power_up_type = DEFAULT_TYPE
        self.power_time_up = 0
        self.shoot_delay = 350  # Balas a medio segundo
        self.last_shoot = pygame.time.get_ticks() 
        #self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self, user_input, bullet_manager):
        key_tasks = { #Asignar teclas a tareas específicas
            pygame.K_LEFT: self.move_left,
            pygame.K_RIGHT: self.move_right,
            pygame.K_UP: self.move_up,
            pygame.K_DOWN: self.move_down,
            pygame.K_SPACE: lambda: self.shoot(bullet_manager)
        }
        for key, task in key_tasks.items():
            if user_input[key]:
                task()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def move_up(self):
        self.rect.y -= self.SPACESHIP_SPEED
        if self.rect.y <0:
            self.rect.y = 0

    def move_down(self):
        self.rect.y += self.SPACESHIP_SPEED
        if self.rect.y >= self.SPACESHIP_POS_Y + 40:
            self.rect.y = self.SPACESHIP_POS_Y + 40

    def move_right(self):
        self.rect.x += 10
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.left = -self.SPACESHIP_WIDTH
    
    def move_left(self):
        self.rect.x -= 10
        if self.rect.left <= 0:
            self.rect.right = SCREEN_WIDTH + self.SPACESHIP_WIDTH

    def shoot(self, bullet_manager):
        now = pygame.time.get_ticks ()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
        sound_player= pygame.mixer.Sound(SOUND_SHOOT)
        sound_player.set_volume(0.1) #control del volumen
        pygame.mixer.Sound.play(sound_player)

    def set_image(self, size = (SCREEN_WIDTH, SCREEN_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.power_up_type = DEFAULT_TYPE
        self.power_time_up = 0
        #self.lives = 0

    def hide (self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT -40)
