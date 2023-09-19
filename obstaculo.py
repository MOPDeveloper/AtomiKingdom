import pygame
class Obstaculos:
    def __init__(self):
        self.tamanho_celula = 40
        self.obstaculos = []
        self.colunas = [160, 320, 480, 640]
        self.linhas = [150, 300, 450]
        self.criar_obstaculos()

    def criar_obstaculos(self):
        for coluna in self.colunas:
            for linha in self.linhas:
                obstaculo = pygame.Rect(coluna, linha, self.tamanho_celula, self.tamanho_celula)
                self.obstaculos.append(obstaculo)

    def desenhar(self, tela):
        for obstaculo in self.obstaculos:
            pygame.draw.rect(tela, (192, 192, 192), obstaculo)