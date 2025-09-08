import pygame

class Aide(pygame.sprite.Sprite):

    def __init__(self,game,x,y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/aide.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def remove(self):
        self.game.all_aides.remove(self)


