import pygame
BLACK = (0, 0, 0)

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino_runner/assets/Dino/DinoRun1.png")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = 300, 200
    def update(self, surface):
        surface.blit(self.image, self.rect)
        
        
pygame.init()

screen = pygame.display.set_mode([1100, 600])
clock = pygame.time.Clock()

done = False

player = Dinosaur()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    player.update(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
