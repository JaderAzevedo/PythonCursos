

# Utilizando o CONSTRUTOR 
# e o __str__ que do Python
 
class Data():
    # Construtor (construtor)
    def __init__(self,dia=1,mes=1,ano=1970):
        self.dia=dia
        self.mes=mes
        self.ano=ano
    #  To string usando o __str__ não sará necessario chamar o método
    def __str__(self): 
        return f'{self.dia}/{self.mes}/{self.ano}'



# d3.dia = 5
# d3.mes = 12
# d3.ano = 2019

d3 = Data(5,12,2019)
print(d3) 

d4=Data(7,11,2020)
print(d4)

d5=Data()  #Ulilizando paramatros padrao
print(d5)


