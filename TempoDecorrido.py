import time
import sys

#TEMPORIZADOR DECRESCENTE
class Temporizador:
    def __init__(self, tempo_total): #Recebe da main o valor do tempo em segundos
        self.tempo_total = tempo_total
        self.tempo_inicial = None

    def iniciar(self):
        self.tempo_inicial = time.time()

    def atualizar(self):
        tempo_decorrido = int(self.tempo_total - (time.time() - self.tempo_inicial))
        if tempo_decorrido == 0:
            sys.exit()
        return tempo_decorrido
    
    def aumentar(self, segundos):
        self.tempo_total+=segundos

