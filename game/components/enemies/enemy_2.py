import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy2(Sprite):
    ENEMY_WIDTH = 60
    ENEMY_HEIGHT = 60
    SPEED_ON_Y = 1
    X_POS_RANGE = range(100, 1001, 100)

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop=(random.choice(self.X_POS_RANGE), - self.ENEMY_WIDTH))
        self.direction = random.choice([-1, 1])  

    def update(self, enemies):
        self.rect.y += self.SPEED_ON_Y
        self.rect.x += self.direction * 10
        
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.direction *= -1
            
        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
