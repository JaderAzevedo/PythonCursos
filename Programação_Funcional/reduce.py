from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]
# Utilizando reduce
soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)
print('--------------------------------------------------------------------')


# Utilizando reduce e filter para pessoas menores
menores = filter(lambda p: p['idade'] < 18, pessoas)
soma_idades_m = reduce(lambda idades, p: idades + p['idade'], menores, 0)
print(soma_idades_m)

print('--------------------------------------------------------------------')


# Utilizando reduce , filter e map para pessoas menores
so_idades = map(lambda pessoa: pessoa['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idades)
soma_idades_m = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idades_m)
