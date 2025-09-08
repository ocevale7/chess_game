import pygame

class Fleche_aide(pygame.sprite.Sprite):

    def __init__(self,game,pos,place,orientation=0):
        super().__init__()
        if place == "fin":
            self.image = pygame.image.load('assets/fin_fleche.png')
        elif place == "milieu":
            self.image = pygame.image.load('assets/milieu_fleche.png')
        elif place == "debut":
            self.image = pygame.image.load('assets/debut_fleche.png')
        elif place == "tournant":
            self.image = pygame.image.load('assets/angle_fleche.png')
        elif place == "case":
            self.image = pygame.image.load('assets/case.png')
        
        self.origin_image = self.image
        
        self.rotate(orientation)
    
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]*100*game.rapport
        self.rect.y = pos[1]*100*game.rapport
    
    def rotate(self,angle):
        self.image = pygame.transform.rotozoom(self.origin_image,angle, 1)
    
    def remove(self,game):
        game.all_fleches_help.remove(self)
