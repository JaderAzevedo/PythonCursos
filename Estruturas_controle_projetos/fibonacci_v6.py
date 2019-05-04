def fibonacci(quantidade):
    lista = [0, 1]
    # Enquanto o último elemento for menor que o limite
    while True:
        # Soma os 2 últimos elemantos da lista [-2:] e adiciona ao final
        lista.append(sum(lista[-2:]))
        if len(lista) == quantidade:
            break
    return lista


print(fibonacci(20))
print('\n\n\n\n')
for elemento in fibonacci(20):
    print(elemento)
