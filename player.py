import pygame
from bomba import Bomba
from coletaveis import *

class Player(pygame.sprite.Sprite):
    def __init__(self, img, todos_sprites, todas_bombas, todos_players, todos_quebraveis, x, y, largura, altura, conjunto_bomba,gerenciador_de_layout,assets):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()

        #COLOCANDO UM NOME PELA IMAGEM
        if assets == 'assets/kiriku.png':
             self.nome = "player1"
        elif assets == 'assets/esqueleto brabo.png':
             self.nome = "player2"

        #SPRITES E IMAGENS DO JOGADOR E DA BOMBA
        self.image = img
        self.todas_sprites = todos_sprites
        self.todas_bombas = todas_bombas
        self.todos_players = todos_players
        self.todos_quebraveis = todos_quebraveis
        self.rect = self.image.get_rect()
        self.largura =largura
        self.altura = altura
        self.gerenciador = gerenciador_de_layout
    

        #POSIÇÕES 
        self.x = x
        self.y = y
        self.rect.x = x*self.largura
        self.rect.y = y*self.altura

        #CONJUNTO ONDE FICA A IMAGEM DA ANIMAÇÃO DA BOMBA E DA EXPLOSAO
        self.conjunto_bomba = conjunto_bomba

        #SEGUNDOS PARA PODER SOLTAR OUTRA BOMBA
        self.ultima_bomba = pygame.time.get_ticks()
        self.tempo_limite = 3000 #3 SEGUNDOS PARA SOLTAR OUTRA BOMBA

    def update(self):
        # ATUALIZA POSIÇÃO
            self.rect.x = self.x*self.largura
            self.rect.y = self.y*self.altura

    def soltar_bomba(self):
        tempo_atual = pygame.time.get_ticks()

        # SE O TEMPO ATUAL MENOS O TEMPO QUE FOI LANÇADO A ULTIMA BOMBA FOR MAIOR QUE O LIMITE ELE LANÇA OUTRA BOMBA
        if tempo_atual - self.ultima_bomba >= self.tempo_limite:

            #ULTIMA BOMBA VIRA O TEMPO ATUAL E CRIA UMA NOVA BOMVA
            self.ultima_bomba = tempo_atual
            nova_bomba = Bomba(self.conjunto_bomba,self.rect.centerx,self.rect.centery,self.todas_sprites,self.todas_bombas,self.todos_players,self.todos_quebraveis,self.gerenciador,self.nome,self.x,self.y)

            self.todas_bombas.add(nova_bomba)
            self.todas_sprites.add(self.todas_bombas)

    def colidir_coin(self,player):
        colisoes_player = pygame.sprite.spritecollide(player, self.todas_sprites, False)
        for moeda in colisoes_player:
            if isinstance(moeda, Coin):
                moeda.kill()
                return "TrueCoin"
            
    def colidir_freeze(self,player):
        colisoes_player = pygame.sprite.spritecollide(player, self.todas_sprites, False)
        for ice in colisoes_player:
            if isinstance(ice, Freeze):
                ice.kill()
                return True
        return False
        
    def colidir_time(self,player):
        colisoes_player = pygame.sprite.spritecollide(player, self.todas_sprites, False)
        for time in colisoes_player:
            if isinstance(time, Extra_Time):
                time.kill()
                return True
        return False

         
