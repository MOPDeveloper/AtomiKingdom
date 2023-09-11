import pygame

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura = 390
altura = 360
tamanho_celula = 25
# tamanho_quadrado = 40
cor_fundo = (144,238,144)

#passos
passos = 2.5

# Cores
cor_personagem = (0, 0, 255)
cor_obstaculo = (128, 128, 128)
cor_bomba = (255, 0, 0)

# Cria a janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bomberman")

# Define o jogador
player = pygame.Rect(50, 50, tamanho_celula, tamanho_celula)

# Lista de obstáculos
obstaculos = [pygame.Rect(25, 72,tamanho_celula,tamanho_celula),
pygame.Rect(25, 144,tamanho_celula,tamanho_celula),
pygame.Rect(25, 216,tamanho_celula,tamanho_celula),
pygame.Rect(25,288,tamanho_celula,tamanho_celula),
pygame.Rect(100,72,tamanho_celula,tamanho_celula),
pygame.Rect(100,144,tamanho_celula,tamanho_celula),
pygame.Rect(100,216,tamanho_celula,tamanho_celula),
pygame.Rect(100,288,tamanho_celula,tamanho_celula),
pygame.Rect(175,72,tamanho_celula,tamanho_celula),
pygame.Rect(175,144,tamanho_celula,tamanho_celula),
pygame.Rect(175,216,tamanho_celula,tamanho_celula),
pygame.Rect(175,288,tamanho_celula,tamanho_celula),
pygame.Rect(250,72,tamanho_celula,tamanho_celula),
pygame.Rect(250,144,tamanho_celula,tamanho_celula),
pygame.Rect(250,216,tamanho_celula,tamanho_celula),
pygame.Rect(250,288,tamanho_celula,tamanho_celula),
pygame.Rect(325,72,tamanho_celula,tamanho_celula),
pygame.Rect(325,144,tamanho_celula,tamanho_celula),
pygame.Rect(325,216,tamanho_celula,tamanho_celula),
pygame.Rect(325,288,tamanho_celula,tamanho_celula)]

# Lista de bombas
bombas = []

#Posição da bomba fora da tela
pos_bomba = [-100,-100]

#condição para analisar se el está ou não segurando a bomba
bomba_disponivel = True

# Configura o clock do jogo
clock = pygame.time.Clock()

FPS = 90 # Defina a taxa de FPS desejada aqui

# Função para desenhar o jogador, obstáculos e bombas
def desenhar_elementos():
    tela.fill(cor_fundo)
    pygame.draw.rect(tela, cor_personagem, player)
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, cor_obstaculo, obstaculo)
# for bomba in bombas:
# pygame.draw.rect(tela, cor_bomba, bomba)
def desenhar_bomba():
# tela.fill(cor_fundo)
    bomba = pygame.draw.circle(tela,cor_bomba,pos_bomba,10)
    return bomba

#condição para ver se ativou a bomba
bomba_ativada = False

# Loop principal do jogo
# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                if bomba_disponivel:
                    bomba_ativada = True
                    pos_bomba = [player.x+(tamanho_celula/2), player.y+(tamanho_celula/2)]
                    print(pos_bomba)

    # Posição anterior do jogador
    posicao_anterior = player.copy()

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        player.x -= passos
    if teclas[pygame.K_RIGHT]:
        player.x += passos
    if teclas[pygame.K_UP]:
        player.y -= passos
    if teclas[pygame.K_DOWN]:
        player.y += passos



    # Verificar colisões com obstáculos
    for obstaculo in obstaculos:
        if player.colliderect(obstaculo):
            player = posicao_anterior



    # Verificar limites da tela
    player.x = max(0, min(player.x, largura - tamanho_celula))
    player.y = max(0, min(player.y, altura - tamanho_celula))

    # Verificar se o jogador colidiu com uma bomba
    for bomba in bombas:
        if player.colliderect(bomba):
            executando = False

    # Desenha os elementos na tela
    desenhar_elementos()

    # Desenha a bomba se estiver ativada
    if bomba_ativada:
        desenhar_bomba()


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()