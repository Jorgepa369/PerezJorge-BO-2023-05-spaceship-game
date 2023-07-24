import random

import pygame

from game.components.enemies.enemy import Enemy
from game.components.explosion import Explosion
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, SHIELD_TYPE, SOUND_EXPLOSION

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_images = [ENEMY_1, ENEMY_2, ENEMY_3]
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            if enemy.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    #game.player.lives -= 1
                    explode = Explosion(enemy.rect.center)
                    game.all_sprites.add(explode)
                    game.enemy_manager.enemies.remove(enemy)
                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    game.player.hide()
                    
                    sound_explosion = pygame.mixer.Sound(SOUND_EXPLOSION)
                    pygame.mixer.Sound.play(sound_explosion)
                    break

                    '''if game.player.lives==0:
                        game.score_manager.death_count()
                        game.menu.actual_screen = True
                        game.playing = False
                        pygame.time.delay(2000) #IMPORT GAME
                        break'''
                else:
                    game.enemy_manager.enemies.remove(enemy)
                    explode = Explosion(enemy.rect.center)
                    game.all_sprites.add(explode)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
            image = random.choice(self.enemy_images)
            speed_on_x = random.randint(10, 20)
            speed_on_y = random.randint(1, 5)

            enemy = Enemy(image, speed_on_x, speed_on_y)
            self.enemies.append(enemy)
            
    def destroy_enemy(self, bullet,game):
        for enemy in  self.enemies:
            # implementar explosion 
            if enemy.rect.colliderect(bullet.rect):
                self.enemies.remove(enemy)
                explosion = Explosion(enemy.rect.center)
                game.all_sprites.add(explosion)
                score = game.score_manager.update_score()
                game.score_manager.score_list(score)
                return True

    def reset(self):
        self.enemies = []