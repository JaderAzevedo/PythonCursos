class Humano():
    #  atributo de classse
    especie = 'Homo_Sapiens'

    def __init__(self, nome):
        self.nome = nome

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


print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
print(f'Neantental evoluido? {Neanderthal.is_evoluido()}')
print(f'José evoluido? {jose.is_evoluido()}')
print(f'Grokn evoluido? {grokn.is_evoluido()}')
