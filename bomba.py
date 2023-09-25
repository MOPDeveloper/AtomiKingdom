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

        self.conjunto_bomba = conjunto_bomba
        self.image = self.conjunto_bomba[0]
        self.rect = self.image.get_rect()
        self.types= conjunto_bomba
        self.tempo = 100 #TEMPO PARA MUDAR AS IMAGENS DA ANIMAÇÃO, FOI PURA ESPECULAÇÃO E IREMOS TESTAR

    def update(self):
        # AINDA ESTA ADEPTO A MUDANÇAS,POIS NÃO SEI SE O TEMPO DE 1 A SER ELIMINADO A CADA FRAME É SUFICIENTE
        # NEM O TEMPO PARA CADA FOTO MUDAR
        self.tempo-=1

        if self.tempo < 70 and self.tempo>= 50:
            self.image = self.conjunto_bomba[1]

        if self.tempo < 50 and self.tempo>= 25:
            self.image = self.conjunto_bomba[2]

        if self.tempo < 25 and self.tempo>= 0:
            self.image = self.conjunto_bomba[3]
            self.explodir()

    def explodir():
        """COMEÇAR A DESENVOLVER A LOGICA DO CONTATO COM QUEBRAVEIS E PLAYER"""
        pass




        