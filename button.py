import pygame

class Button():
    def __init__(self, imagem, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # COORDENADAS DO BOTÃO
    def coord(self):
        self.rect.topleft = self.x, self.y

    
    def pressed(self,posx,posy,top,bottom):
        if posx in range(247, 503) and posy in range(top, bottom):
            return True
        return False
    
    def show_button(self, place):
        place.blit(self.image, (self.x, self.y))

    
