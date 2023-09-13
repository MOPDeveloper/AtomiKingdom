import pygame
import random
import math

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Coletor de Moedas')

# Cores
branco = (255, 255, 255)
amarelo = (255, 255, 0)

class Jogo:
    def __init__(self):
        self.player = pygame.Rect(50, 50, 40, 40)
        self.player_speed = 2
        self.moeda = pygame.Rect(0, 0, 20, 20)
        self.contagem_moedas = 0
        self.nova_moeda()

    def nova_moeda(self):
        self.moeda.x = random.randint(0, largura - 20)
        self.moeda.y = random.randint(0, altura - 20)

    def atualizar(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Movimento do jogador com base nas teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.player.x -= self.player_speed
        if teclas[pygame.K_RIGHT]:
            self.player.x += self.player_speed
        if teclas[pygame.K_UP]:
            self.player.y -= self.player_speed
        if teclas[pygame.K_DOWN]:
            self.player.y += self.player_speed

        # Verifica a colisão entre o jogador e a moeda
        if self.player.colliderect(self.moeda):
            self.contagem_moedas += 1
            self.nova_moeda()

    def desenhar(self):
        tela.fill(branco)

        # Desenha o jogador
        pygame.draw.rect(tela, amarelo, self.player)

        # Desenha a moeda
        pygame.draw.ellipse(tela, amarelo, self.moeda)

        # Exibe a contagem de moedas
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(f"Moedas: {self.contagem_moedas}", True, amarelo)
        tela.blit(texto, (10, 10))

        # Atualiza a tela
        pygame.display.update()

# Instanciar o jogo
jogo = Jogo()

# Loop principal do jogo
while True:
    jogo.atualizar()
    jogo.desenhar()
