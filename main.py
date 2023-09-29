import pygame
import sys
from brick import Brick
import random 
from quebravel import Bloco_q
from player import Player
import pygame.mixer #garantindo uma bela canção
from TempoDecorrido import Temporizador
from coletaveis import Coin, Extra_Time, Freeze

pygame.mixer.init()
pygame.mixer.music.load('assets/esqueleto - kelvis duran.mp3')
pygame.mixer.music.set_volume(0.00)

pygame.init()

#FPS DO JOGO
clock = pygame.time.Clock()
FPS = 30
temporizador = Temporizador(120)

#MEDIDAS DO JOGO
WIDTH = 750
HEIGHT = 700
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Rise Of LequeLeto')

#CONSTANTES DE ALTURA E LARGURA
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 40
BRICK_WIDTH=50
BRICK_HEIGHT=50
QUEBRAVEL_WIDTH=50
QUEBRAVEL_HEIGHT=50
BOMB_WIDTH=65
BOMB_HEIGHT=65
EXP_WIDTH=100
EXP_HEIGHT=100

player1_img = pygame.image.load('assets/kiriku.png')
kiriku = 'assets/kiriku.png'
esqueleto = 'assets/esqueleto brabo.png'
player1_img = pygame.transform.scale(player1_img, (BRICK_WIDTH, BRICK_HEIGHT))
player2_img = pygame.image.load('assets/esqueleto brabo.png')
player2_img = pygame.transform.scale(player2_img, (BRICK_WIDTH, BRICK_HEIGHT))
bomb1_img = pygame.image.load('assets/000.png')
bomb1_img = pygame.transform.scale(bomb1_img, (BOMB_WIDTH,BOMB_HEIGHT))
bomb2_img = pygame.image.load('assets/001.png')
bomb2_img = pygame.transform.scale(bomb2_img, (BOMB_WIDTH,BOMB_HEIGHT))
bomb3_img = pygame.image.load('assets/002.png')
bomb3_img = pygame.transform.scale(bomb3_img, (BOMB_WIDTH,BOMB_HEIGHT))
bomb4_img = pygame.image.load('assets/003.png')
bomb4_img = pygame.transform.scale(bomb4_img, (BOMB_WIDTH,BOMB_HEIGHT))
conjunto_bomba = [bomb1_img,bomb2_img,bomb3_img,bomb4_img]
coin_img = pygame.image.load('assets/coin.png')
coin_img = pygame.transform.scale(coin_img, (BRICK_WIDTH, BRICK_HEIGHT))
freeze_img=pygame.image.load('assets/freeze.png')
freeze_img=pygame.transform.scale(freeze_img, (BRICK_WIDTH, BRICK_HEIGHT))
add_time_img=pygame.image.load('assets/add_time.png')
add_time_img = pygame.transform.scale(add_time_img, (BRICK_WIDTH, BRICK_HEIGHT))

"""LÓGICA DO JOGO EM FORMA DE MATRIZ
0 - ESPAÇO VAZIO OU BLOCO QUEBRAVEL
1 - BLOCO FIXO
4 - ESPAÇO PARA O TIMER
5 - PLAYER1
6 - PLAYER2 
7 - MOEDA
9 - LUGARES QUE NÃO PODEM SER BLOO QUEBRAVEIS"""

class Gerenciador_Layout:
    def __init__(self):

        self.LAYOUT = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1],
    [1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 6, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 7, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 8, 1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 7, 1, 0, 1, 0, 1, 7, 1, 0, 1, 0, 1, 7, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1, 8, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 8, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 5, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1],
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
freeze_1 = 0
freeze_2 = 0 
times_1 = 0
times_2 = 0
coins_player1=0
coins_player2=0 
jogador1_congelado = False
tempo_congelamento1 = 0 
jogador2_congelado = False
tempo_congelamento2 = 0 

gerenciador = Gerenciador_Layout()

def desenhar_mapa():
    global player1, player2, coins_player1, coins_player2
    

    for l in range (len(gerenciador.LAYOUT)):
            for c in range (len(gerenciador.LAYOUT[l])):
                item = gerenciador.LAYOUT[l][c]
                
                if item == 1:
                    pedra = Brick(c,l,BRICK_WIDTH,BRICK_HEIGHT)
                    todos_fixos.add(pedra)
                
                if item == 0:
                    r= random.randint(2,4)
                    if r ==3 or r==4:
                        madeira = Bloco_q(c,l,QUEBRAVEL_WIDTH,QUEBRAVEL_HEIGHT)
                        todos_quebraveis.add(madeira)
                        gerenciador.LAYOUT[l][c] = 1
                    else:
                        gerenciador.LAYOUT[l][c] = 0

                if item == 4 :
                    gerenciador.LAYOUT[l][c] = 0
                if item == 5 :

                    gerenciador.LAYOUT[l][c] = 0
            
                    player1 = Player(player1_img, todos_sprites, todas_bombas,todos_players,todos_quebraveis,c,l,BRICK_WIDTH,BRICK_HEIGHT,conjunto_bomba,gerenciador,kiriku)
                    todos_sprites.add(player1)
                    todos_players.add(player1)
               


                if item == 6:
                    gerenciador.LAYOUT[l][c] = 0
                    player2 = Player(player2_img,todos_sprites, todas_bombas,todos_players,todos_quebraveis,c,l,BRICK_WIDTH,BRICK_HEIGHT,conjunto_bomba,gerenciador,esqueleto)
                    todos_sprites.add(player2)
                    todos_players.add(player2)

                #Definindo Moeda
                if item==7:
                    gerenciador.LAYOUT[l][c] = 0
                    coin = Coin(coin_img,c,l,QUEBRAVEL_WIDTH,QUEBRAVEL_HEIGHT)
                    todos_sprites.add(coin)
                
                #Definindo Freeze
                if item==8:
                    gerenciador.LAYOUT[l][c] = 0
                    freeze = Freeze(freeze_img,c,l,QUEBRAVEL_WIDTH,QUEBRAVEL_HEIGHT)
                    todos_sprites.add(freeze)

                #Definindo Add Time
                if item==2:
                    gerenciador.LAYOUT[l][c] = 0
                    add_time = Extra_Time(add_time_img,c,l,QUEBRAVEL_WIDTH,QUEBRAVEL_HEIGHT)
                    todos_sprites.add(add_time)

# adicionando aos grupos de sprites
todos_sprites.add(todos_players)
todos_sprites.add(todos_fixos)
todos_sprites.add(todos_quebraveis)
todos_blocos.add(todos_fixos)
todos_blocos.add(todos_quebraveis)
desenhar_mapa()


def desenhar_temporizador(tempo_decorrido):
    fonte = pygame.font.Font('assets/Minecraft.ttf', 30)
    texto = fonte.render(f"Tempo: {tempo_decorrido} s", True, (16,28,64))
    tela.blit(texto, (550, 15))

def desenhar_moedas_player1(coins_player1):
    fonte = pygame.font.Font('assets/Minecraft.ttf', 15)
    texto = fonte.render(f"Moedas Player 1: {coins_player1} ", True, (16,28,64))
    tela.blit(texto, (1, 1))

def desenhar_moedas_player2(coins_player2):
    fonte = pygame.font.Font('assets/Minecraft.ttf', 15)
    texto = fonte.render(f"Moedas Player 2: {coins_player2} ", True, (16,28,64))
    tela.blit(texto, (1, 30))

    # PALETA DE CORES DO QUEBRAVEL
    # 46,78,140
    #  39, 65, 140
    # 31, 52, 115
    16,28,64
    # 10, 17, 38

def jogo():
    global freeze_1, freeze_2, times_1, times_2, coins_player1,coins_player2,jogador1_congelado,tempo_congelamento1,jogador2_congelado,tempo_congelamento2
    
    pygame.mixer.music.play(-1)
    jogo = True
    temporizador.iniciar() #INICIALIZA O TEMPORIZADOR QUANDO RODA O JOGO
    while jogo:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.music.stop()
                sys.exit()

        # Tratamento de eventos de teclado
            if event.type == pygame.KEYDOWN:
                if not jogador1_congelado:
                    if event.key == pygame.K_UP:
                        if gerenciador.LAYOUT[player1.y - 1][player1.x] == 0 or gerenciador.LAYOUT[player1.y - 1][player1.x] == 9:
                            player1.y -= 1  # Mova o jogador para cima
                    elif event.key == pygame.K_DOWN:
                        if gerenciador.LAYOUT[player1.y + 1][player1.x] == 0 or gerenciador.LAYOUT[player1.y + 1][player1.x] == 9:
                            player1.y += 1  # Mova o jogador para baixo
                    elif event.key == pygame.K_LEFT:
                        if gerenciador.LAYOUT[player1.y][player1.x - 1] == 0 or gerenciador.LAYOUT[player1.y][player1.x - 1] == 9:
                            player1.x -= 1  # Mova o jogador para a esquerda
                    elif event.key == pygame.K_RIGHT: 
                        if gerenciador.LAYOUT[player1.y][player1.x + 1] in[0,9]:
                            player1.x += 1
                    elif event.key == pygame.K_RSHIFT:
                        player1.soltar_bomba()
    
            #TECLADO DO SEGUNDO JOGADOR
                if not jogador2_congelado:
                    if event.key == pygame.K_w:
                        if gerenciador.LAYOUT[player2.y - 1][player2.x] == 0 or gerenciador.LAYOUT[player2.y - 1][player2.x] == 9:
                            player2.y -= 1 # Mova o jogador para cima
                    elif event.key == pygame.K_s:
                        if gerenciador.LAYOUT[player2.y + 1][player2.x] == 0 or gerenciador.LAYOUT[player2.y + 1][player2.x] == 9:
                            player2.y += 1  # Mova o jogador para baixo
                    elif event.key == pygame.K_a:
                        if gerenciador.LAYOUT[player2.y][player2.x - 1] == 0 or gerenciador.LAYOUT[player2.y][player2.x - 1] == 9:
                            player2.x -= 1  # Mova o jogador para a esquerda
                    elif event.key == pygame.K_d: 
                        if gerenciador.LAYOUT[player2.y][player2.x + 1] in[0,9]:
                            player2.x += 1
                    elif event.key == pygame.K_f:
                        player2.soltar_bomba()

	    # Verifique se o jogador 1 colidiu com uma moeda
        colisoes_player1 = pygame.sprite.spritecollide(player1, todos_sprites, False)
        for moeda in colisoes_player1:
            if isinstance(moeda, Coin):
                coins_player1 += 1
                moeda.kill()  # Remove a moeda
         # Verifique se o jogador 2 colidiu com uma moeda
        colisoes_player2 = pygame.sprite.spritecollide(player2, todos_sprites, False)
        for moeda in colisoes_player2:
            if isinstance(moeda, Coin):
                coins_player2 += 1
                moeda.kill()  # Remove a moeda
        
        def determinar_vencedor(coins_player1, coins_player2):
            if coins_player1 > coins_player2:
                return "Player 1"
            elif coins_player2 > coins_player1:
                return "Player 2"
            else:
                return "Empate"

        # Verifique se o jogador 1 colidiu com freeze
        colisoes_player1 = pygame.sprite.spritecollide(player1, todos_sprites, False)
        
        for ice in colisoes_player1:
            if isinstance(ice, Freeze):
                ice.kill() 
                freeze_1 += 1
                jogador2_congelado = True
                tempo_congelamento2 = 100

         # Verifique se o jogador 2 colidiu com freeze
        colisoes_player2 = pygame.sprite.spritecollide(player2, todos_sprites, False)
        for ice in colisoes_player2:
            if isinstance(ice, Freeze):
                ice.kill()  
                freeze_2 += 1
                jogador1_congelado = True
                tempo_congelamento1 = 160
        
        # Reduza o tempo de congelamento
        if jogador1_congelado:
            tempo_congelamento1 -= 1

            # Se o tempo de congelamento terminou, descongele o jogador 2
            if tempo_congelamento1 <= 0:
                jogador1_congelado = False    
        # Reduza o tempo de congelamento
        if jogador2_congelado:
            tempo_congelamento2 -= 1

            # Se o tempo de congelamento terminou, descongele o jogador 2
            if tempo_congelamento2 <= 0:
                jogador2_congelado = False

        # Verifique se o jogador 1 colidiu com add_time
        colisoes_player1 = pygame.sprite.spritecollide(player1, todos_sprites, False)

        for time in colisoes_player1:
            if isinstance(time, Extra_Time):
                times_1 += 1
                time.kill() 
                temporizador.aumentar(6)
        # Verifique se o jogador 2 colidiu com add_time
        colisoes_player2 = pygame.sprite.spritecollide(player2, todos_sprites, False)
        for time in colisoes_player2:
            if isinstance(time, Extra_Time):
                times_2 += 1
                time.kill()  
                temporizador.aumentar(6)
        
        #TRATANDO COLETAVEIS PARA A APRESENTACAO DE P1
        def desenhar_freeze_player1(freeze_1):
            fonte = pygame.font.Font('assets/Minecraft.ttf', 15)
            texto = fonte.render(f"Freeze Player 1: {freeze_1} ", True, (16,28,64))
            tela.blit(texto, (160, 1))  
        def desenhar_freeze_player2(freeze_2):
            fonte = pygame.font.Font('assets/Minecraft.ttf', 15)
            texto = fonte.render(f"Freeze Player 2: {freeze_2} ", True, (16,28,64))
            tela.blit(texto, (160, 30))  
        
        def desenhar_times_player1(times_1):
            fonte = pygame.font.Font('assets/Minecraft.ttf', 15)
            texto = fonte.render(f"Extra Times Player 1: {times_1} ", True, (16,28,64))
            tela.blit(texto, (320, 1))  
        def desenhar_times_player2(times_2):
            fonte = pygame.font.Font('assets/Minecraft.ttf', 15)
            texto = fonte.render(f"Extra Times Player 2: {times_2} ", True, (16,28,64))
            tela.blit(texto, (320, 30)) 


        # Atualize a posição do jogador
        player1.update()
        player2.update()
        todos_sprites.update()
        todas_bombas.update()

        tela.fill((144, 238, 144))  # PREENCHER A TELA DE VERDE

        # Desenha os blocos
        todos_fixos.draw(tela)
        todos_quebraveis.draw(tela)
        todas_bombas.draw(tela)
        todos_sprites.draw(tela)
        # Obtenha o tempo decorrido do temporizador
        tempo_decorrido = temporizador.atualizar()
        if tempo_decorrido == 0:
            vencedor = determinar_vencedor(coins_player1, coins_player2)
            if vencedor == 'Player 1':
                fonte = pygame.font.Font('assets/Minecraft.ttf', 100)
                texto = fonte.render(f"PLAYER 1 WINS", True, (0,0,0))
                tela.blit(texto, (0, 325))
            elif vencedor == 'Player 2':
                fonte = pygame.font.Font('assets/Minecraft.ttf', 100)
                texto = fonte.render(f"PLAYER 2 WINS", True, (0,0,0))
                tela.blit(texto, (0, 325))
            else:
                fonte = pygame.font.Font('assets/Minecraft.ttf', 100)
                texto = fonte.render(f"EMPATE", True, (0,0,0))
                tela.blit(texto, (200, 325))
                
        # Desenhe o temporizador
        desenhar_freeze_player1(freeze_1)
        desenhar_freeze_player2(freeze_2)
        desenhar_times_player1(times_1)
        desenhar_times_player2(times_2)
        desenhar_temporizador(tempo_decorrido)
        desenhar_moedas_player1(coins_player1)
        desenhar_moedas_player2(coins_player2)
        pygame.display.update()  # Atualiza a tela

jogo()  # Chama a função para iniciar o loop do jogo
