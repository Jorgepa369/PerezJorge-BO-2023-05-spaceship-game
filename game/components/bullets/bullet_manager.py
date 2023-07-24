import time
import pygame
from game.components.explosion import Explosion
from game.utils.constants import SHIELD_TYPE, SOUND_EXPLOSION
class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.last_bullet_time = time.time()
    
    def update(self, game, enemy_manager):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                if game.player.power_up_type != SHIELD_TYPE:
                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    game.player.hide()
                    
                    sound_explosion = pygame.mixer.Sound(SOUND_EXPLOSION)
                    pygame.mixer.Sound.play(sound_explosion)
                    break
                    #game.player.lives -= 1
                    '''if game.player.lives == 0:
                        game.score_manager.death_count()
                        game.player.lives = 3
                        game.menu.actual_screen = True
                        game.playing = False
                        pygame.time.delay(2000)            
                        break'''
        
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            delete = enemy_manager.destroy_enemy(bullet, game)
            if delete:
                self.player_bullets.remove(bullet)
                sound_explosion = pygame.mixer.Sound(SOUND_EXPLOSION)
                pygame.mixer.Sound.play(sound_explosion)

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy':
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' :
            self.player_bullets.append(bullet)
            self.last_bullet_time = time.time ()

    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []