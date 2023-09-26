import pygame
from quebravel import Bloco_q
# from player import Player

class Bomba(pygame.sprite.Sprite):
    def __init__(self,conjunto_bomba,x,y,todos_sprites,todas_bombas,todos_players,todos_quebraveis,layout,nome_player):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()

        #SPRITES
        self.todos_sprites = todos_sprites
        self.todas_bombas = todas_bombas
        self.todos_players = todos_players
        self.todos_quebraveis = todos_quebraveis
        self.nome = nome_player

        #POSIÇÕES
        self.x = x
        self.y = y

        #IMAGENS E LAYOUT
        self.conjunto_bomba = conjunto_bomba
        self.image = self.conjunto_bomba[0]
        self.rect = self.image.get_rect()
        self.types= conjunto_bomba
        self.layout = layout
        self.rect.centerx = x
        self.rect.centery = y

        self.tempo = 120 #TEMPO PARA MUDAR AS IMAGENS DA ANIMAÇÃO, FOI PURA ESPECULAÇÃO E IREMOS TESTAR

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

    def explodir(self):
        """COMEÇAR A DESENVOLVER A LOGICA DO CONTATO COM QUEBRAVEIS E PLAYER"""
        colidir_quebravel = pygame.sprite.groupcollide(self.todas_bombas,self.todos_quebraveis,False,False)
        print(colidir_quebravel)
        #COLODIR QUEBRAVEL É UM DICIONARIO COM A BOMBA QUE BATEU E OS VALORES SÃO UMA LISA DOS QUEBRAVEIS
        for quebraveis in colidir_quebravel:
                locais_possiveis = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y+ 1), (self.x, self.y - 1)]

                if isinstance(quebraveis,Bloco_q):
                     if (quebraveis.x,quebraveis.y) in locais_possiveis:
                          self.layout[quebraveis.x][quebraveis.y] = 0
                          quebraveis.kill()


        # colidir_player = pygame.sprite.groupcollide(self.todas_bombas,self.todos_players,False,False)
        # #COLODIR QUEBRAVEL É UM DICIONARIO COM A BOMBA QUE BATEU E OS VALORES SÃO UMA LISA DOS QUEBRAVEIS
        # for players in colidir_player:
        #         #LOCAIS POSSIVEIS É A EXPANSÃO DA BOMBA
        #         locais_possiveis = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y+ 1), (self.x, self.y - 1)]

        #         if isinstance(players,Player):
        #              if (players.x,players.y) in locais_possiveis:
        #                     self.layout[players.x][players.y] = 0
        #                     if self.nome == "player1": #IDENTIFICAÇÃO QUAL É O PLAYER
        #                         if players == self.nome:
        #                             """AINDA NÃO FOI CRIADO A FUNÇÃO DA VITORIA"""
        #                             # win(self.nome)
        #                             players.kill()
        #                         else:
        #                             # win(self.nome)
        #                             players.kill()

        self.kill()
        pass




        