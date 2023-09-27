import time

#TEMPORIZADOR DECRESCENTE
class Temporizador:
    def __init__(self, tempo_total): #Recebe da main o valor do tempo em segundos
        self.tempo_total = tempo_total
        self.tempo_inicial = None

    def iniciar(self):
        self.tempo_inicial = time.time()

    def atualizar(self):
        tempo_decorrido = int(self.tempo_total - (time.time() - self.tempo_inicial))
        if tempo_decorrido < 0:
            tempo_decorrido = 0
        return tempo_decorrido

# TINHA TENTADO FAZER UM CONTADOR DECRESCENTE DE UMA FORMA MAIS SIMPLES, E CONSEGUI, MAS NÃO CONSEGUI DESENHAR NA TELA.
# import time
#
# for x in range(120, 0, -1):
#     segundos = x % 60
#     minutos = int(x/60) % 60
#     print (f"{minutos:02}:{segundos:02}")
#     time.sleep(1)
