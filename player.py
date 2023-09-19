import pygame
from obstaculo import Obstaculos

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 40, 40)
        self.speed = 7

    def mover(self, teclas, obstaculos):
        # Salve a posição anterior do jogador
        posicao_anterior = self.rect.copy()

        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if teclas[pygame.K_UP]:
            self.rect.y -= self.speed
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Verifique colisões com os obstáculos
        for obstaculo in obstaculos.obstaculos:
            if self.rect.colliderect(obstaculo):
                # Reverta o movimento do jogador para a posição anterior
                self.rect = posicao_anterior

    def limites(self, largura, altura):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura:
            self.rect.bottom = altura

    def desenhar(self, tela):
        pygame.draw.rect(tela, (0, 255, 0), self.rect)
