import pygame
import sys
import constantes
import layout
import random
import pygame.mixer
from layout import GerenciadorLayout
from brick import Brick
from quebravel import Bloco_q
from player import Player
from tempoDecorrido import Temporizador
from coletaveis import Coin, Extra_Time, Freeze

pygame.mixer.init()
pygame.mixer.music.load('assets/esqueleto - kelvis duran.mp3')
pygame.mixer.music.set_volume(1.00)

pygame.init()

#FPS DO JOGO
clock = pygame.time.Clock()
FPS = 30
temporizador = Temporizador(120)

#Tela
tela = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))

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

gerenciador = GerenciadorLayout()

def desenhar_mapa():
    global player1, player2, coins_player1, coins_player2
    

    for l in range (len(gerenciador.LAYOUT)):
            for c in range (len(gerenciador.LAYOUT[l])):
                item = gerenciador.LAYOUT[l][c]

                if item == 0:
                    r= random.randint(2,4)
                    if r ==3 or r==4:
                        madeira = Bloco_q(c, l, constantes.QUEBRAVEL_WIDTH, constantes.QUEBRAVEL_HEIGHT)
                        todos_quebraveis.add(madeira)
                        gerenciador.LAYOUT[l][c] = 1
                    else:
                        gerenciador.LAYOUT[l][c] = 0
                
                if item == 1:
                    pedra = Brick(c, l, constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT)
                    todos_fixos.add(pedra)

                #Definindo Add Time
                if item == 2:
                    gerenciador.LAYOUT[l][c] = 0
                    add_time = Extra_Time(layout.add_time_img, c, l, constantes.QUEBRAVEL_WIDTH,
                                          constantes.QUEBRAVEL_HEIGHT)
                    todos_sprites.add(add_time)

                if item == 4 :
                    gerenciador.LAYOUT[l][c] = 0

                if item == 5 :
                    gerenciador.LAYOUT[l][c] = 0
                    player1 = Player(layout.player1_img, todos_sprites, todas_bombas, todos_players, todos_quebraveis, c, l,
                                     constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT, gerenciador, layout.kiriku)
                    todos_sprites.add(player1)
                    todos_players.add(player1)


                if item == 6:
                    gerenciador.LAYOUT[l][c] = 0
                    player2 = Player(layout.player2_img, todos_sprites, todas_bombas, todos_players, todos_quebraveis, c, l,
                                     constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT, gerenciador, layout.esqueleto)
                    todos_sprites.add(player2)
                    todos_players.add(player2)

                #Definindo Moeda
                if item==7:
                    gerenciador.LAYOUT[l][c] = 0
                    coin = Coin(layout.coin_img, c, l, constantes.QUEBRAVEL_WIDTH, constantes.QUEBRAVEL_HEIGHT)
                    todos_sprites.add(coin)
                
                #Definindo Freeze
                if item==8:
                    gerenciador.LAYOUT[l][c] = 0
                    freeze = Freeze(layout.freeze_img, c, l, constantes.QUEBRAVEL_WIDTH, constantes.QUEBRAVEL_HEIGHT)
                    todos_sprites.add(freeze)


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
        if player1.colidir_coin(player1) == "TrueCoin":
            coins_player1 += 1
         # Verifique se o jogador 2 colidiu com uma moeda
        if player2.colidir_coin(player2) == "TrueCoin":
            coins_player2 += 1
        
        def determinar_vencedor(coins_player1, coins_player2):
            if coins_player1 > coins_player2:
                return "Player 1"
            elif coins_player2 > coins_player1:
                return "Player 2"
            else:
                return "Empate"

        # Verifique se o jogador 1 colidiu com freeze
        if player1.colidir_freeze(player1) == True:
            freeze_1 += 1
            jogador2_congelado = True
            tempo_congelamento2 = 100
        # Verifique se o jogador 2 colidiu com freeze 
        if player2.colidir_freeze(player2) == True:
            freeze_2 += 1
            jogador1_congelado = True
            tempo_congelamento1 = 100
        
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
        if player1.colidir_time(player1) == True:
            times_1 += 1
            temporizador.aumentar(6)
        # Verifique se o jogador 2 colidiu com add_time
        if player2.colidir_time(player2) == True:
            times_2 += 1
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


        #VERIFICAÇÃO DE QUAL PLAYER VENCEU OU NÃO
        if len(todos_players) == 1:
            vencedor = todos_players.sprites()[0]
            imagem_vencedor =vencedor.image

            if imagem_vencedor == layout.player1_img:
                win(player1)
            elif imagem_vencedor == layout.player2_img:
                win(player2)

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
                win(player1)
            elif vencedor == 'Player 2':
                win(player2)
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

def win(player):
    while True:
        pygame.display.set_caption('Fim de jogo')
        tela.fill((0, 255, 100))
        kiriku_grande = pygame.transform.scale(layout.player1_img, (100, 100))
        letoleto_grande = pygame.transform.scale(layout.player2_img, (100, 100))

        if player == player1:
            tela.blit(layout.floresta, (0,0))
            tela.blit(kiriku_grande,(310,320))
            fonte = pygame.font.Font('assets/Minecraft.ttf', 50)
            texto = fonte.render(f"KIRIKU VENCEU", True, (91,140,77,55))
            #(148,190,76,75)
            (91,140,77,55)
            #(140,217,119,59)
            tela.blit(texto, (200, 240))
        elif player == player2:
            tela.blit(layout.cemiterio, (0,0))
            tela.blit(letoleto_grande,(310,320))
            fonte = pygame.font.Font('assets/Minecraft.ttf', 50)
            texto = fonte.render(f"LETOLETO VENCEU", True, (255,255,255))
            tela.blit(texto, (150, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        

jogo()  # Chama a função para iniciar o loop do jogo
