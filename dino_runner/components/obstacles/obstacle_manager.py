import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS,BIRD

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, game):

        if len(self.obstacles) == 0:
            type = random.randint(0,2)
            match type:
                case 0:
                    self.obstacles.append(Bird(BIRD))
                case 1:
                    self.obstacles.append(Cactus(SMALL_CACTUS))
                case 2:
                    self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.hammer:
                    game.heart_manager.reduce_heart()
                elif not game.player.shield:
                    game.heart_manager.reduce_heart()
                if game.heart_manager.heart_count < 1:
                    game.game_over.gameisover()
                    pygame.time.delay(1500)
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
