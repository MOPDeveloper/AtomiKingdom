import pygame

class Button():
    def __init__(self,x, y):
        self.image = pygame.image.load('assets/jogar_button.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def show_button(self, tela):
        tela.blit(self.image, (self.x, self.y))
        
    def pressed(self,posx,posy,top,bottom):
        if posx in range(247, 503) and posy in range(top, bottom):
            return True
        return False
    
    
    
