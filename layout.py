import pygame
import constantes

"""LÓGICA DO JOGO EM FORMA DE MATRIZ
0 - ESPAÇO VAZIO OU BLOCO QUEBRAVEL
1 - BLOCO FIXO
4 - ESPAÇO PARA O TIMER
5 - PLAYER1
6 - PLAYER2 
7 - MOEDA
9 - LUGARES QUE NÃO PODEM SER BLOO QUEBRAVEIS"""


class GerenciadorLayout:
    def __init__(self):
        self.LAYOUT = [
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 6, 1],
            [1, 0, 1, 8, 1, 0, 1, 0, 1, 0, 1, 0, 1, 9, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 7, 1, 0, 1, 0, 1, 7, 1, 0, 1, 0, 1, 7, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1, 8, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 9, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 5, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]


# TELAS FINAIS DO JOGO
floresta = pygame.image.load('assets/floresta.png')
floresta = pygame.transform.scale(floresta, (constantes.WIDTH, constantes.HEIGHT))
cemiterio = pygame.image.load('assets/cemiterio2.png')
cemiterio = pygame.transform.scale(cemiterio, (constantes.WIDTH, constantes.HEIGHT))

#SPRITES DO JOGO
player1_img = pygame.image.load('assets/kiriku.png')
kiriku = 'assets/kiriku.png'
esqueleto = 'assets/esqueleto brabo.png'
player1_img = pygame.transform.scale(player1_img, (constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT))
player2_img = pygame.image.load('assets/esqueleto brabo.png')
player2_img = pygame.transform.scale(player2_img, (constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT))
coin_img = pygame.image.load('assets/coin.png')
coin_img = pygame.transform.scale(coin_img, (constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT))
freeze_img=pygame.image.load('assets/freeze.png')
freeze_img=pygame.transform.scale(freeze_img, (constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT))
add_time_img=pygame.image.load('assets/add_time.png')
add_time_img = pygame.transform.scale(add_time_img, (constantes.BRICK_WIDTH, constantes.BRICK_HEIGHT))
