import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Coletor de Moedas')

# Cores
branco = (255, 255, 255)
amarelo = (255, 255, 0)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 40, 40)
        self.speed = 1.5

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if teclas[pygame.K_UP]:
            self.rect.y -= self.speed
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.speed

class Moeda:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.nova_posicao()

    def nova_posicao(self):
        self.rect.x = random.randint(0, largura - 20)
        self.rect.y = random.randint(0, altura - 20)

class Jogo:
    def __init__(self):
        self.player = Player()
        self.moeda = Moeda()
        self.contagem_moedas = 0

    def atualizar(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        teclas = pygame.key.get_pressed()
        self.player.mover(teclas)

        if self.player.rect.colliderect(self.moeda.rect):
            self.contagem_moedas += 1
            self.moeda.nova_posicao()

    def desenhar(self):
        tela.fill(branco)

        pygame.draw.rect(tela, amarelo, self.player.rect)
        pygame.draw.ellipse(tela, amarelo, self.moeda.rect)

        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(f"Moedas: {self.contagem_moedas}", True, amarelo)
        tela.blit(texto, (10, 10))

        pygame.display.update()

# Instanciar o jogo
jogo = Jogo()

# Loop principal do jogo
while True:
    jogo.atualizar()
    jogo.desenhar()
