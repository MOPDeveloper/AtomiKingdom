import time


class Temporizador:
    def __init__(self, tempo_total):
        self.tempo_total = tempo_total
        self.tempo_inicial = None
        self.encerrado = False

    def iniciar(self):
        self.tempo_inicial = time.time()

    def atualizar(self):
        if self.tempo_inicial is not None and not self.encerrado: 
            tempo_decorrido = int(self.tempo_total - (time.time() - self.tempo_inicial))
            if tempo_decorrido <= 0:
                self.encerrado = True
                return 0  # O tempo acabou
            return tempo_decorrido
        return 0

    def aumentar(self, segundos):
        self.tempo_total += segundos
    
    def encerrado(self): #pra poder verificar quem ganhou qnd o game acaba
        return self.encerrado
