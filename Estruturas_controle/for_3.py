produto = {'nome': 'Caneta chic', 'preço': 14.99,
           'importado': True, 'estoque': 793}


for chave in produto:
    print(chave)
print('-'*70)
for valor in produto.values():
    print(valor)
print('-'*70)

for chave, valor in produto.items():
    print(chave, ':', valor)
print('-'*70)
