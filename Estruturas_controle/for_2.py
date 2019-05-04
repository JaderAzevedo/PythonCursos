palavra = 'paralelepípado'

for letra in palavra:
    print(letra, end=',')
print('\nFim')
print('-'*70)


aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)
print('-'*70)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao+1}) ', nome)
print('-'*70)


for numero in {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}:  # Conjunto (set)
    print(numero)
