def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2

#  Retorna alternadamente a função dobro e a função quadrado de x


# Utilizando funções como dados
funcs = [dobro, quadrado]*5
#  Utilizando a função ZIP
for funcao, numero in zip(funcs, range(1, 11)):
    print(f'O {funcao.__name__} de {numero} é {funcao(numero)}')

# Utilizando funções como dados
d = dobro

print(d(5))

# Utilizando funções como dados
q = quadrado

print(q(5))
