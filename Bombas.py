import pygame
from obstaculo import Obstaculos

class Bomba:
    """
    Classe da Bomba

    """
    def __init__(self,x,y):
        """self.x = x
        self.y = y"""
        self.largura = 20
        self.comprimento = 20
        self.quadrado = pygame.Rect(x,y,self.largura,self.comprimento)
        self.rect = self.quadrado
        self.expandiu = False

        self.obstaculos = Obstaculos()

        self.tempo = 2500 #SEGUNDOS PARA A BOMBA EXPLODIR
        self.color = (255,0,0)

        self.left = False
        self.right = False
        self.up = False
        self.down = False

    """CALCULA O TEMPO PARA EXPLODIR"""
    def atualizar(self):
        agora = pygame.time.get_ticks()
        #VAI VERIFICAR SE PASSOU O TEMPO QUE A BOMBA TEM QUE EXPLODIR
        if agora >= self.tempo:
            self.expandiu = True
            self.explosao = self.calcular_explosao()
            return self.explosao


    """FUNÇÃO QUE VAI VERIFICAR SE A EXPANSÃO DA BOMBA BATEU EM ALGUM BLOCO INQUEBRAVEL"""
    def colisao_inquebravel(self,rect):
       # Verifique se o retângulo colide com obstáculos do jogo
        for obstaculo in self.obstaculos.obstaculos: #PEGUEI A LISTA DE OBSTACULOS DA CLASSE OBSTACULO
            if rect.colliderect(obstaculo):
                return True
        return False


    def calcular_explosao(self):
        #LISTA QUE CONTEM OS RETANGULOS DA EXPANSAO DA EXPLOSÃO
        explosao = []

        """RETANGULOS DA EXPLOSÃO"""
        left_rect = pygame.Rect(self.rect.left - 20, self.rect.top, self.largura, self.comprimento)
        right_rect = pygame.Rect(self.rect.left + 20, self.rect.top, self.largura, self.comprimento)
        up_rect = pygame.Rect(self.rect.left, self.rect.top - 20, self.largura, self.comprimento)
        down_rect = pygame.Rect(self.rect.left, self.rect.top + 20, self.largura, self.comprimento)

        # Verifique se os retângulos da explosão colidem com obstáculos
        if not self.colisao_inquebravel(left_rect):
            explosao.append(left_rect)
        else:
            #PARA VERIFICAR QUE NAQUELE LADO HOUVE COLISAO
            explosao.append("erro")

        if not self.colisao_inquebravel(right_rect):
            explosao.append(right_rect)
        else:
            #PARA VERIFICAR QUE NAQUELE LADO HOUVE COLISAO
            explosao.append("erro")

        if not self.colisao_inquebravel(up_rect):
            explosao.append(up_rect)
        else:
            #PARA VERIFICAR QUE NAQUELE LADO HOUVE COLISAO
            explosao.append("erro")

        if not self.colisao_inquebravel(down_rect):
            explosao.append(down_rect)
        else:
            #PARA VERIFICAR QUE NAQUELE LADO HOUVE COLISAO
            explosao.append("erro")

        
        return explosao
	
    def desenhar(self,x,y,tela):
        pygame.draw.rect(tela, self.color, self.rect)
        #MOSTRAR A BOMBA
        expansao = self.atualizar()
        if self.expandiu:
            for bomba in expansao:
                #SE A BOMBA FOR "0" SIGNIFICA QUE ALI HOUVE COLISAO COM INQUEBRAVEL
                if bomba =="erro":
                    pass
                else:
                    pygame.draw.rect(tela, self.color, bomba)

