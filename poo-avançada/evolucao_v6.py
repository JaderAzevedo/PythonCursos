from abc import ABCMeta, abstractproperty


class Humano(metaclass=ABCMeta):
    #  atributo de classse
    especie = 'Homo_Sapiens'

    # -------------------------------------------------------------------------
    # Construtor
    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # Métodos GET e SET utilizando Propriedades
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser positiva')
        self._idade = idade
    # -------------------------------------------------------------------------
    #  Técnica da definir classe abstrata em Python,
    # que não é suportada nativamente

    @abstractproperty
    def inteligente(self):
        pass

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',)+tuple(f'Homo {adj}'for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):  # Por padrão se usa o cls de classe
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


# Agora só podemos instanciar as classes concretas
# try:
#     anonimo = Humano('John Doe')
#     print(anonimo.inteligente)
# except TypeError:
#     print('Classe Abstrata')

jose = HomoSapiens('José')

print('{} da clase {}, inteligente{}'.format(
    jose.nome, jose.__class__.__name__, jose.inteligente))
