class ClasseSimples:
    #  Contar a quantidade de objetos "instanciados"
    contador = 0

    def __init__(self):
        self.contar()
        #  Poderia ser usado o modo baixo sem o médoto contar
        #  self.__class__.contador += 1

    @classmethod
    def contar(cls):
        cls.contador += 1


lista = [ClasseSimples(), ClasseSimples()]
print(ClasseSimples.contador)
