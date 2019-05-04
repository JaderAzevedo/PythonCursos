class Humano():
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


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


jose = HomoSapiens('José')

grokn = Neanderthal('Grokn')

jose = HomoSapiens('José')
jose.idade = 40
print(f'Nome: {jose.nome}   Idade: {jose.idade}')
