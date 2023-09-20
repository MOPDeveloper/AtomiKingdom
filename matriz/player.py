import pygame

class Player:
    def __init__(self,img,todos_sprites,todas_bombas,x,y,largura,altura):
        pygame.sprite.Sprite.__init__(self)

        #SPRITES E IMAGENS DO JOGADOR E DA BOMBA
        self.imagem = img
        self.todas_sprites = todos_sprites
        self.todas_bombas = todas_bombas
        self.rect = self.imagem.get_rect()
        
        #POSIÇÕES 
        self.x = x
        self.y = y
        self.rect.x = x*largura
        self.rect.y = y*altura

        #SEGUNDOS PARA PODER SOLTAR OUTRA BOMBA
        self.bomba_solta = pygame.time.get_ticks()
        self.tempo_limite = 3000 #3 SEGUNDOS PARA SOLTAR OUTRA BOMBA