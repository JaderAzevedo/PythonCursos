class Carro:
    #  contrutor
    # Recebe apenas a velocidade máxima

    def __init__(self,velocidade_máxima):
        self.velocidade_máxima=velocidade_máxima
        self.velocidade_atual=0

    def acelerar(self, delta=5):
        maxima=self.velocidade_máxima
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova<= maxima else maxima
        return self.velocidade_atual

    def frear (self,delta=5):
        nova = self.velocidade_atual -delta
        self.velocidade_atual= nova if nova >= 0 else 0
        return self.velocidade_atual

Carro1 = Carro(180)

for _ in range(25):  #  omitindo o parametro com '_'
    print(Carro1.acelerar(8))
for _ in range(10):
    print(Carro1.frear(20))

    
