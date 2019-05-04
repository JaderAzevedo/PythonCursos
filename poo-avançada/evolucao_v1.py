class Humano():
    #  atributo de classse
    especie = 'Homo_Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'


jose = Humano('José')

grokn = Humano('Grokn')
grokn.das_cavernas()

#  Não deu certo
# grokn = Humano('Grokn').das_cavernas()

print(f'Humano.espécie: {Humano.especie}')
print(f'José.espécie: {jose.especie}')
print(f'Grokn.espécie: {grokn.especie}')
