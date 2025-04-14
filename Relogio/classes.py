
import time

class Relogio:
    tempo = 0

    def __init__(self,tempo):
        self.tempo = tempo


    def contar_progressivo (self, on, speed=1, limite = 100):
        print ("Contagem Progressiva: ")
        while on:    
            self.tempo += 1
            time.sleep(speed)
            Relogio.mostrar(self)
            if (self.tempo) > limite:
                print("ACABOU TEMPO")
                break


    def contar_regressivo (self, on,speed=1):
        print ("Contagem Regressiva :")
        while on:
            self.tempo -= 1
            time.sleep(speed)
            Relogio.mostrar(self)
            if (self.tempo) < 0:
                print("ACABOU TEMPO")
                break



    def mostrar (self):
        horas = self.tempo // 3600
        resto = self.tempo % 3600
        min = resto // 60
        seg = self.tempo % 60
        print (f"{horas:02}:{min:02}:{seg:02}",end='\r')
    # def pausar(tempo):
