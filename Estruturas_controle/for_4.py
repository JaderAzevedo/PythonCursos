from random import randint
for i in range(1, 11):
    if i == 5:
        break               # Sai do for.
    print(i)
else:
    print('Fim')
print('-'*70)
# -----------------------------------------------------------------------------


def sortear_dado():
    return randint(1, 10)     # Sortear numro de 1 ao "10" '


for i in range(1, 7):
    if i % 2 == 1:         # Verificar se é impar
        continue

    if sortear_dado() == i:
        print('Acertou', i)
        break
else:
    print('Não acertou')
