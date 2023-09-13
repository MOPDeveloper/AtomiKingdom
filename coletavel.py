import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Coletor de Moedas')
# Cores
branco = (0, 0, 0)
verde = (0, 255, 0)
azul = (0,0,255)
vermelho = (255,0,0)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 40, 40)
        self.speed = 1

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

class Moeda:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.nova_posicao()

    def nova_posicao(self):
        self.rect.x = random.randint(0, largura - 20)
        self.rect.y = random.randint(0, altura - 20)

class MoedaAzul:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.nova_posicao()

    def nova_posicao(self):
        self.rect.x = random.randint(0, largura - 20)
        self.rect.y = random.randint(0, altura - 20)

class MoedaVermelha:
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
        self.moedaazul = MoedaAzul()
        self.moedavermelha = MoedaVermelha()
        self.contagem_moedas = 0
        self.contagem_moedasAzul = 0
        self.contagem_moedasVermelhas = 0

    def atualizar(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        teclas = pygame.key.get_pressed()
        self.player.mover(teclas)
        self.player.limites(largura=largura, altura=altura)

        if self.player.rect.colliderect(self.moeda.rect):
            self.contagem_moedas += 1
            self.moeda.nova_posicao()
        
        if self.player.rect.colliderect(self.moedavermelha.rect):
            self.contagem_moedasVermelhas += 1
            self.moedavermelha.nova_posicao()
        
        if self.player.rect.colliderect(self.moedaazul.rect):
            self.contagem_moedasAzul += 1
            self.moedaazul.nova_posicao()

    def desenhar(self):
        tela.fill(branco)

        pygame.draw.rect(tela, verde, self.player.rect)
        pygame.draw.ellipse(tela, verde, self.moeda.rect)
        pygame.draw.ellipse(tela, azul, self.moedaazul.rect)
        pygame.draw.ellipse(tela, vermelho, self.moedavermelha.rect)



        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(f"Moedas Verdes: {self.contagem_moedas}", True, verde)
        texto2 = fonte.render(f"Moedas Azuis: {self.contagem_moedasAzul}", True, azul)
        texto3 = fonte.render(f"Moedas Vermelhas: {self.contagem_moedasVermelhas}", True, vermelho)


        tela.blit(texto, (10, 10))
        tela.blit(texto2, (250, 10))
        tela.blit(texto3, (500, 10))


        pygame.display.update()
# Instanciar o jogo
jogo = Jogo()

# Loop principal do jogo
while True:
    
    jogo.atualizar()
    jogo.desenhar()
    
