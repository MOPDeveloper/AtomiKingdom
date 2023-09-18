import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 40, 40)
        self.speed = 7

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if teclas[pygame.K_UP]:
            self.rect.y -= self.speed
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.speed

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
