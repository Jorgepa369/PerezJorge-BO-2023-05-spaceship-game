import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 40
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/track2.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

MISILE = pygame.image.load(os.path.join(IMG_DIR, 'Other/misile.png'))

MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/BG_menu.png'))
SCORE = pygame.image.load(os.path.join(IMG_DIR, 'Other/fondoscore.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

EXPLOSION_ANIM = []
for i in range(1, 20):
    file = 'Explosion/{}.png'.format(i)
    img = pygame.image.load(os.path.join(IMG_DIR, file))
    img = pygame.transform.scale(img, (110, 110))
    EXPLOSION_ANIM.append(img)
  
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))

SOUND_SHOOT = os.path.join(IMG_DIR, 'Sounds/laserShoot.wav')
SOUND_EXPLOSION = os.path.join(IMG_DIR, 'Sounds/explosion.wav')


FONT_STYLE = 'freesansbold.ttf'