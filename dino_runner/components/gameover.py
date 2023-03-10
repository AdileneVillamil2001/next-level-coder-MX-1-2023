import pygame
from dino_runner.utils.constants import GAMEOVER,SCREEN_HEIGHT,SCREEN_WIDTH

class GameOver_manager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x_pos_GO = 350
        self.y_pos_GO = 300

    def gameisover(self):
        self.screen.fill((255, 255, 255))
        image_width = GAMEOVER.get_width()
        self.screen.blit(GAMEOVER, (self.x_pos_GO, self.y_pos_GO))
        pygame.display.update() #update objects inside
        pygame.display.flip() 