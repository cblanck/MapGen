import pygame, os

class Tile(pygame.sprite.Sprite):
    def __init__(self, group, image = "flower.jpg"):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.image.load(os.path.join('tiles', image)).convert()
        self.rect = self.image.get_rect()
         
