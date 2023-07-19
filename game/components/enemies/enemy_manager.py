import pygame
from game.components.enemies.enemy_1 import Enemy1
from game.components.enemies.enemy_2 import Enemy2

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy1 = Enemy1()
            self.enemies.append(enemy1)
            enemy2 = Enemy2()
            self.enemies.append(enemy2)
            
    