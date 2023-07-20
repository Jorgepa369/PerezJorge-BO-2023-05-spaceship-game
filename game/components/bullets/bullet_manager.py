import pygame

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
    
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(2000)
                break
            
            for bullet in self.player_bullets:
                bullet.update(self.player_bullets)
                
                for enemy in game.enemy_manager.enemies:
                    if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                        self.player_bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy':
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.player_bullets) < 3 :
            self.player_bullets.append(bullet)