import pygame
import sys
from brick import Brick
import random 
from quebravel import Bloco_q
from player import Player
import pygame.mixer 
from coin import Coin

#Definindo o som do Jogo
pygame.mixer.init()
pygame.mixer.music.load('assets/esqueleto - kelvis duran.mp3')
pygame.mixer.music.set_volume(0.25)

pygame.init()

#FPS DO JOGO
clock = pygame.time.Clock()
FPS = 30

#MEDIDAS DO JOGO
WIDTH = 750
HEIGHT = 650
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Rise Of LequeLeto')

#CONSTANTES DE ALTURA E LARGURA
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 40
BRICK_WIDTH=50
BRICK_HEIGHT=50
QUEBRAVEL_WIDTH=50
QUEBRAVEL_HEIGHT=50
BOMB_WIDTH=90
BOMB_HEIGHT=90
EXP_WIDTH=100
EXP_HEIGHT=100

#IMAGENS DOS BLOCOS E PERSONAGENS
brick_img = pygame.image.load('assets/Bloco_Fixo.png')
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT))
quebravel_img = pygame.image.load('assets/quebravel.png')
quebravel_img =  pygame.transform.scale(quebravel_img, (QUEBRAVEL_WIDTH, QUEBRAVEL_HEIGHT))
player1_img = pygame.image.load('assets/kiriku.png')
player1_img = pygame.transform.scale(player1_img, (BRICK_WIDTH, BRICK_HEIGHT))
player2_img = pygame.image.load('assets/esqueleto brabo.png')
player2_img = pygame.transform.scale(player2_img, (BRICK_WIDTH, BRICK_HEIGHT))
coin_img = pygame.image.load('assets/coin.png')
coin_img = pygame.transform.scale(coin_img, (BRICK_WIDTH, BRICK_HEIGHT))
conjunto_bomba = []


"""LÓGICA DO JOGO EM FORMA DE MATRIZ"""
LAYOUT = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 6, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 9, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 7, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 9, 1, 0, 1, 7, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 5, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]



# Criando um grupo de blocos 
todos_quebraveis = pygame.sprite.Group()
todos_fixos = pygame.sprite.Group()
todos_blocos = pygame.sprite.Group()

# Criando um grupo de sprites
todos_sprites = pygame.sprite.Group()
todas_bombas = pygame.sprite.Group()
todos_players = pygame.sprite.Group()


player1 = None  
player2 = None  
coins_player1=0
coins_player2=0

def desenhar_mapa():
    global player1, player2, coins_player1, coins_player2

    for l in range (len(LAYOUT)):
            for c in range (len(LAYOUT[l])):
                item = LAYOUT[l][c]
                
                #Definindo os blocos de Pedras que não podem ser quebrados
                if item == 1:
                    pedra = Brick(brick_img,c,l,BRICK_WIDTH,BRICK_HEIGHT)
                    todos_fixos.add(pedra)
                
                
                if item == 0:
                    r= random.randint(2,4)
                    if r ==3 or r==4:
                        #Definindo os blocos de madeira que podem ser quebrados pela bomba
                        madeira = Bloco_q(quebravel_img,c,l,QUEBRAVEL_WIDTH,QUEBRAVEL_HEIGHT)
                        todos_quebraveis.add(madeira)
                        LAYOUT[l][c] = 1
                    else:
                        LAYOUT[l][c] = 0

                #Definindo o jogador 1
                if item == 5 :
                    LAYOUT[l][c] = 0
                    player1 = Player(player1_img, todos_sprites, todas_bombas,todos_players,todos_quebraveis,c,l,BRICK_WIDTH,BRICK_HEIGHT,conjunto_bomba)
                    todos_sprites.add(player1)
                    
               

                #Definindo o Jogador 2
                if item == 6:
                    LAYOUT[l][c] = 0
                    player2 = Player(player2_img,todos_sprites, todas_bombas,todos_players,todos_quebraveis,c,l,BRICK_WIDTH,BRICK_HEIGHT,conjunto_bomba)
                    todos_sprites.add(player2)
                    

                #Definindo Moeda
                if item==7:
                    LAYOUT[l][c] = 0
                    coin = Coin(coin_img,c,l,QUEBRAVEL_WIDTH,QUEBRAVEL_HEIGHT)
                    todos_sprites.add(coin)




# adicionando aos grupos de sprites
todos_sprites.add(todos_players)
todos_sprites.add(todos_fixos)
todos_sprites.add(todos_quebraveis)
todos_blocos.add(todos_fixos)
todos_blocos.add(todos_quebraveis)
desenhar_mapa()
def jogo():
    global coins_player1,coins_player2
    pygame.mixer.music.play(-1)
    jogo = True
    while jogo:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.music.stop()
                sys.exit()
        
        # Tratamento de eventos de teclado
            #Movimento Player1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if LAYOUT[player1.y - 1][player1.x] == 0 or LAYOUT[player1.y - 1][player1.x] == 9:
                        player1.y -= 1  # Mova o jogador para cima
                elif event.key == pygame.K_DOWN:
                    if LAYOUT[player1.y + 1][player1.x] == 0 or LAYOUT[player1.y + 1][player1.x] == 9:
                        player1.y += 1  # Mova o jogador para baixo
                elif event.key == pygame.K_LEFT:
                    if LAYOUT[player1.y][player1.x - 1] == 0 or LAYOUT[player1.y][player1.x - 1] == 9:
                        player1.x -= 1  # Mova o jogador para a esquerda
                elif event.key == pygame.K_RIGHT: 
                    if LAYOUT[player1.y][player1.x + 1] in[0,9]:
                        player1.x += 1
            
            #Movimento Player2
                if event.key == pygame.K_w:
                    if LAYOUT[player2.y - 1][player2.x] == 0 or LAYOUT[player2.y - 1][player2.x] == 9:
                        player2.y -= 1  # Mova o jogador para cima
                elif event.key == pygame.K_s:
                    if LAYOUT[player2.y + 1][player2.x] == 0 or LAYOUT[player2.y + 1][player2.x] == 9:
                        player2.y += 1  # Mova o jogador para baixo
                elif event.key == pygame.K_a:
                    if LAYOUT[player2.y][player2.x - 1] == 0 or LAYOUT[player2.y][player2.x - 1] == 9:
                        player2.x -= 1  # Mova o jogador para a esquerda
                elif event.key == pygame.K_d: 
                    if LAYOUT[player2.y][player2.x + 1] in[0,9]:
                        player2.x += 1
        # Verifique se o jogador 1 colidiu com uma moeda
        colisoes_player1 = pygame.sprite.spritecollide(player1, todos_sprites, False)
        for moeda in colisoes_player1:
            if isinstance(moeda, Coin):
                coins_player1 += 1
                moeda.kill()  # Remove a moeda
                print(f"O Kelvis tem {coins_player1} moedas")
         # Verifique se o jogador 2 colidiu com uma moeda
        colisoes_player2 = pygame.sprite.spritecollide(player2, todos_sprites, False)
        for moeda in colisoes_player2:
            if isinstance(moeda, Coin):
                coins_player2 += 1
                moeda.kill()  # Remove a moeda
        # Atualize a posição do jogador
        player1.update()
        player2.update()

        tela.fill((144, 238, 144))  # PREENCHER A TELA DE VERDE

        # Desenha os blocos
        todos_fixos.draw(tela)
        todos_quebraveis.draw(tela)
        todos_sprites.draw(tela)
        pygame.display.update()  # Atualiza a tela

jogo()  # Chama a função para iniciar o loop do jogo
