import pygame

class Fleche_retour(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.image = pygame.image.load('assets/fleche_left.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(1020*game.rapport)
        self.rect.y = int(370*game.rapport)

class Fleche_avance(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.image = pygame.image.load('assets/fleche_right.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(1120*game.rapport)
        self.rect.y = int(370*game.rapport)

class Fleche_retour_n(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.image = pygame.image.load('assets/fleche_left_n.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(1020*game.rapport)
        self.rect.y = int(370*game.rapport)

class Fleche_avance_n(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.image = pygame.image.load('assets/fleche_right_n.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(1120*game.rapport)
        self.rect.y = int(370*game.rapport)

class Fleche_tourne(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.image = pygame.image.load('assets/fleche_tourne.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(920*game.rapport)
        self.rect.y = int(370*game.rapport)
