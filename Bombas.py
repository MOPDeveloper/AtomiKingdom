import pygame

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
        self.active = False

        self.tempo = 2.5
        self.color = "vermelho"

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.posições = []

    """def active_bomb(self,x,y):
        self.rect.center = (x,y)
        self.active = True"""

    """FUNÇÃO QUE VAI VERIFICAR SE A EXPANSÃO DA BOMBA BATEU EM ALGUM BLOCO INQUEBRAVEL"""
    def colisao_inquebravel(self,x,y,bloco_inquebravel,largura,comprimento):
        avanço_fogo = pygame.Rect(x,y,largura,comprimento)
        if avanço_fogo.collidedict(bloco_inquebravel):
            return True


    def alcance(self,x,y,bloco_inquebravel):
        #VERIFICAÇÃO da EXPANSÃO DO FOGO PARA O LADO ESQUERDO
        condition = colisao_inquebravel(x-20,y,bloco_inquebravel,self.largura,self.comprimento)
        if condition:
            self.left = True
    
        #VERIFICAÇÃO PARA O LADO DIREITO
        condition = colisao_inquebravel(x+20,y,bloco_inquebravel,self.largura,self.comprimento)
        if condition:
            self.right = True

        #VERIFICAÇÃO PARA CIMA
        condition = colisao_inquebravel(x,y-20,bloco_inquebravel,self.largura,self.comprimento)
        if condition:
            self.up = True

        #VERIFICAÇÃO PARA BAIXO
        condition = colisao_inquebravel(x,y+20,bloco_inquebravel,self.largura,self.comprimento)
        if condition:
            self.down = True

        self.posições.append(self.left,self.right,self.up,self.down)
	
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.color, self.rect)
