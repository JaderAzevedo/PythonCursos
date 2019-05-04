def fibonacci(quantidade):
    lista = [0, 1]

    for i in range(2, quantidade):
        # Soma os 2 últimos elemantos da lista [-2:] e adiciona ao final
        lista.append(sum(lista[-2:]))
    return lista


print(fibonacci(20))
print('\n\n\n\n')
for elemento in fibonacci(20):
    print(elemento)
