
class Data:
    #  To string
    def to_str(self): 
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019

print(d1.to_str())

d2=Data()
d2.dia=7
d2.mes=11
d2.ano = 2020

print(d2.to_str())

#----------------------------------------------------------------------------------------------------
# utilizando o __str__ que do Python 

class DataPython:
    #  To string usando o __str__ não sará necessario chamar o método
    def __str__(self): 
        return f'{self.dia}/{self.mes}/{self.ano}'


d3 = DataPython()
d3.dia = 5
d3.mes = 12
d3.ano = 2019

print(d3) #  Não é necessario escrever o método

d4=DataPython()
d4.dia=7
d4.mes=11
d4.ano = 2020

print(d4)
