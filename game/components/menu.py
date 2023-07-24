import pygame

from game.utils.constants import FONT_STYLE, MENU, SCORE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDTH = SCREEN_WIDTH / 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 15)
        self.text = self.font.render(message, True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT)
        self.actual_screen = False
        self.score = 0
        self.high_score = 0
        self.deaths = 0
    
    def update(self, game):
        pygame.display.update()
        self.handle_events_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        if self.actual_screen:
            screen.blit(self.score, self.text_rect2)
            screen.blit(self.high_score, self.text_rect3)
            screen.blit(self.deaths, self.text_rect4)
    
    def handle_events_menu(self, game):
        user_input = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif user_input[pygame.K_RETURN]:
                game.run()
    
    def reset_screen_color(self, screen, death_counter):
            if death_counter == 0:
                image = pygame.transform.scale(MENU, (SCREEN_WIDTH, SCREEN_HEIGHT))
            else:
                image = pygame.transform.scale(SCORE, (SCREEN_WIDTH, SCREEN_HEIGHT))
                
            screen.blit(image, (0, 0))
    
    def update_message(self, message):
        self.text = self.font.render(message, True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.SCREEN_HALF_WIDTH + 100, self.SCREEN_HALF_HEIGHT +1000)

    def show_scores(self, score, high_score, deaths):
        self.score = self.font.render("Your score: " + score, True, (255,255,255))
        self.text_rect2 = self.score.get_rect()
        self.text_rect2.center = (self.SCREEN_HALF_WIDTH , self.SCREEN_HALF_HEIGHT + 5)

        self.high_score = self.font.render("Highest score: " + high_score, True, (255,255,255))
        self.text_rect3 = self.high_score.get_rect()
        self.text_rect3.center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT + 50)

        self.deaths = self.font.render("Total deaths: " + deaths, True, (255,255,255))
        self.text_rect4 = self.score.get_rect()
        self.text_rect4.center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT + 100)