import pygame
from quebravel import Bloco_q
# from player import Player

class Bomba(pygame.sprite.Sprite):
    def __init__(self,x,y,todos_sprites,todas_bombas,todos_players,todos_quebraveis,gerenciador,nome_player,i,j):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()

        #SPRITES
        self.todos_sprites = todos_sprites
        self.todas_bombas = todas_bombas
        self.todos_players = todos_players
        self.todos_quebraveis = todos_quebraveis
        self.nome = nome_player
        self.BOMB_WIDTH = 65
        self.BOMB_HEIGHT = 65
        self.bomb1_img = pygame.image.load('assets/000.png')
        self.bomb1_img = pygame.transform.scale(self.bomb1_img, (self.BOMB_WIDTH,self.BOMB_HEIGHT))
        self.bomb2_img = pygame.image.load('assets/001.png')
        self.bomb2_img = pygame.transform.scale(self.bomb2_img, (self.BOMB_WIDTH,self.BOMB_HEIGHT))
        self.bomb3_img = pygame.image.load('assets/002.png')
        self.bomb3_img = pygame.transform.scale(self.bomb3_img, (self.BOMB_WIDTH,self.BOMB_HEIGHT))
        self.bomb4_img = pygame.image.load('assets/003.png')
        self.bomb4_img = pygame.transform.scale(self.bomb4_img, (self.BOMB_WIDTH,self.BOMB_HEIGHT))
        self.conjunto_bomba = [self.bomb1_img,self.bomb2_img,self.bomb3_img,self.bomb4_img]
        self.explosao = pygame.mixer.Sound("assets/explosao.mp3")
        self.explosao.set_volume(0.05)

        #POSIÇÕES
        self.x = x
        self.y = y

        #POSIÇÕES MATRIZ
        self.i = i
        self.j = j

        #IMAGENS E LAYOUT
        # self.conjunto_bomba = conjunto_bomba
        self.image = self.conjunto_bomba[0]
        self.rect = self.image.get_rect()
        self.types= self.conjunto_bomba
        self.gerenciador = gerenciador
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
            self.explosao.play()
            self.explodir()

    def explodir(self):
        """COMEÇAR A DESENVOLVER A LOGICA DO CONTATO COM QUEBRAVEIS E PLAYER"""
        colidir_quebravel = pygame.sprite.groupcollide(self.todas_bombas,self.todos_quebraveis,False,False)

        #COLODIR QUEBRAVEL É UM DICIONARIO COM A BOMBA QUE BATEU E OS VALORES SÃO UMA LISA DOS QUEBRAVEIS
        for bomba, quebraveis in colidir_quebravel.items():
            
            locais_possiveis = [(self.i + 1, self.j), (self.i - 1, self.j), (self.i, self.j+ 1), (self.i, self.j - 1)]

            for quebrado in quebraveis:
                if (quebrado.x,quebrado.y) in locais_possiveis:
                    self.gerenciador.LAYOUT[quebrado.y][quebrado.x] = 0
                    quebrado.kill()


        colidir_player = pygame.sprite.groupcollide(self.todas_bombas,self.todos_players,False,False)
        #COLODIR QUEBRAVEL É UM DICIONARIO COM A BOMBA QUE BATEU E OS VALORES SÃO UMA LISA DOS QUEBRAVEIS
        for bomba,players in colidir_player.items():
                #LOCAIS POSSIVEIS É A EXPANSÃO DA BOMBA
                locais_possiveis = [(self.i + 1, self.j), (self.i - 1, self.j), (self.i, self.j+ 1), (self.i, self.j - 1), (self.i, self.j)]

                for player in players:
                     if (player.x,player.y) in locais_possiveis:
                            self.gerenciador.LAYOUT[player.y][player.x] = 0
                            
                            if self.nome == "player1": #IDENTIFICAÇÃO QUAL É O PLAYER
                                    print(self.nome)
                                    player.kill()
                            if self.nome == "player2": #IDENTIFICAÇÃO QUAL É O PLAYER
                                    print(self.nome)
                                    player.kill()

        self.kill()
        pass




        
