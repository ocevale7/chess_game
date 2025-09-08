import pygame

class win(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/gagnant.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 250

class nul(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/nulle.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 250