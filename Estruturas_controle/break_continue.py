# Impressão de números ímpares

for x in range(1, 11):  # De 1 e 10
    if x % 2 == 0:       # Se resto da disisão é 0
        continue        # Pula para o próximo x
    print(x)

print('\n\n\n\n')

for x in range(1, 11):  # De 1 e 10
    if x == 5:
        break           # Sai da interação
    print(x)

print('-'*70)
