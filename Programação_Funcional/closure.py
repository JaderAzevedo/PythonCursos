def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


dobro = multiplicar(2)
triplo = multiplicar(3)

print(f'O dobro de 3 é {dobro(7)}')
print(f'O triplo de 3 é {triplo(3)}')