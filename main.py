import pygame
from Bombas import Bomba
from Moedas import Moeda, MoedaAzul, MoedaVermelha
from player import Player

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Coletor de Moedas')
# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
cinza = (192, 192, 192)
preto = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 90

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

    def desenhar_obstaculos(self, tela):
        for obstaculo in self.obstaculos:
            pygame.draw.rect(tela, cinza, obstaculo)

            # Verifique a colisão com o jogador para impedir atravessar
            if jogo.player.rect.colliderect(obstaculo):
                if not jogo.colidiu_com_obstaculo:  # Verifique a colisão apenas uma vez
                    if jogo.player.rect.left < obstaculo.right and jogo.player.rect.right > obstaculo.left:
                        if jogo.player.rect.top < obstaculo.bottom and jogo.player.rect.bottom > obstaculo.top:
                            if jogo.player.rect.right - obstaculo.left <= obstaculo.right - jogo.player.rect.left:
                                jogo.player.rect.right = obstaculo.left
                            else:
                                jogo.player.rect.left = obstaculo.right
                        else:
                            if jogo.player.rect.bottom - obstaculo.top <= obstaculo.bottom - jogo.player.rect.top:
                                jogo.player.rect.bottom = obstaculo.top
                            else:
                                jogo.player.rect.top = obstaculo.bottom
                    jogo.colidiu_com_obstaculo = True

"""class Bomba:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)  # Tamanho da bomba
        self.color = vermelho  # Cor da bomba

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.color, self.rect)"""


class Jogo:
    def __init__(self):
        self.player = Player()
        self.moeda = Moeda()
        self.moedaazul = MoedaAzul()
        self.moedavermelha = MoedaVermelha()
        self.contagem_moedas = 0
        self.contagem_moedasAzul = 0
        self.contagem_moedasVermelhas = 0

        self.bomba = None  # Variável para armazenar a bomba
        self.bomba_ativa = False  # Variável de controle para saber se a bomba está ativa

        # Inicialize a lista de obstáculos usando a classe Obstaculos
        self.obstaculos = Obstaculos()

        self.colidiu_com_obstaculo = False  # Variável de controle

    def atualizar(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                # Cria uma instância da bomba no lugar do jogador
                self.bomba = Bomba(self.player.rect.x+ 20, self.player.rect.y + 20)
                self.bomba_ativa = True

        teclas = pygame.key.get_pressed()
        if not self.colidiu_com_obstaculo:  # Verifique colisão apenas se não colidiu antes
            self.player.mover(teclas)
            self.player.limites(largura=largura, altura=altura)

        # Quando todas as teclas são soltas, redefina a variável de controle
        if not any(teclas):
            self.colidiu_com_obstaculo = False

        if self.player.rect.colliderect(self.moeda.rect):
            self.contagem_moedas += 1
            self.moeda.nova_posicao()

        if self.player.rect.colliderect(self.moedavermelha.rect):
            self.contagem_moedasVermelhas += 1
            self.moedavermelha.nova_posicao()

        if self.player.rect.colliderect(self.moedaazul.rect):
            self.contagem_moedasAzul += 1
            self.moedaazul.nova_posicao()
            self.player.speed += 1

        clock = pygame.time.Clock()
        FPS = 90
        clock.tick(FPS)

    #Desenhando os objetos
    def desenhar(self):
        tela.fill(preto)
        self.player.desenhar(tela)
        self.moeda.desenhar(tela)
        self.moedaazul.desenhar(tela)
        self.moedavermelha.desenhar(tela)
        self.obstaculos.desenhar_obstaculos(tela)

        if self.bomba_ativa:
            self.bomba.desenhar(tela)
            

        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(f"Moedas Verdes: {self.contagem_moedas}", True, verde)
        texto2 = fonte.render(f"Bônus Velocidade: {self.contagem_moedasAzul}", True, azul)
        texto3 = fonte.render(f"Moedas Vermelhas: {self.contagem_moedasVermelhas}", True, vermelho)

        tela.blit(texto, (10, 10))
        tela.blit(texto2, (250, 10))
        tela.blit(texto3, (530, 10))

        pygame.display.update()

# Instanciar o jogo
jogo = Jogo()

# Loop principal do jogo
while True:
    jogo.atualizar()
    jogo.desenhar()

    pygame.display.flip()
