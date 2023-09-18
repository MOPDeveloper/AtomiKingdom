import pygame
import random
largura, altura = 800, 600

class Moeda:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.nova_posicao()

    def nova_posicao(self):
        self.rect.x = random.randint(0, largura - 20)
        self.rect.y = random.randint(0, altura - 20)
    
    def desenhar(self, tela):
        pygame.draw.ellipse(tela, (0, 255, 0), self.rect)

class MoedaAzul: #SPEED
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.nova_posicao()

    def nova_posicao(self):
        self.rect.x = random.randint(0, largura - 20)
        self.rect.y = random.randint(0, altura - 20)

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, (0, 0, 255), self.rect)

class MoedaVermelha:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.nova_posicao()

    def nova_posicao(self):
        self.rect.x = random.randint(0, largura - 20)
        self.rect.y = random.randint(0, altura - 20)

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, (255, 0, 0), self.rect)
