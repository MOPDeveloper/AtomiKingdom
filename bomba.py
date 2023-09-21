import pygame

class Bomba:
    def __init__(self,conjunto_bomba,x,y,todos_sprites,todas_bombas,todos_players,todos_quebraveis):
        pygame.sprite.Sprite.__init__(self)

        #SPRITES
        self.todos_sprites = todos_sprites
        self.todas_bombas = todas_bombas
        self.todos_players = todos_players
        self.todos_quebraveis = todos_quebraveis

        #POSIÇÕES
        self.x = x
        self.y = y

        self.image = conjunto_bomba[0]
        self.rect = self.image.get_rect()
        self.types= conjunto_bomba

        