def soma_n(*numeros):  # packing
    soma = 0
    for n in numeros:
        soma += n
    return soma


# packing
print(soma_n(1, 2, 3, 5, 6, 4, 8, 9,))
# unpacking
print(soma_n(*range(0, 100)))
