from random import randint


numero_informado = -1
numero_secreto = randint(0, 10)    # Sorteia um número de 0 a 9


while numero_informado != numero_secreto:
    numero_informado = int(input('Digite o número (0 a 9): '))

print(f'O número secreto{numero_secreto} foi encontrado')
