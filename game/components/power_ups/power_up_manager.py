import pygame
import random
from game.components.explosion import Explosion
from game.components.power_ups.misile import Misile

from game.components.power_ups.shield import Shield
from game.utils.constants import SHIELD_TYPE, SPACESHIP_SHIELD

class PowerUpManager:
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000
    
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3, 5)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            #implementar en game y player
            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                #implementar en game y player
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 2000)
                if game.player.power_up_type == SHIELD_TYPE:
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups = []
                    '''elif game.player.power_up_type == "Heart":
                    game.player.lives += 1
                    self.power_ups = []'''
                elif game.player.power_up_type == "Misile":
                    for enemy in game.enemy_manager.enemies:
                        explode = Explosion(enemy.rect.center)
                        game.all_sprites.add(explode)
                    game.enemy_manager.enemies = []
                    self.power_ups = []
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up = Shield()
        #heart = Heart()
        misile = Misile()
        self.when_appears += random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.power_ups.append(power_up)
        #self.power_ups.append(heart)
        self.power_ups.append(misile)

    def reset(self):
        power_up = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)