def fibonacci(limite):
    lista = [0, 1]
    # Enquanto o último elemento for menor que o limite
    while lista[-1] < limite:
        # Soma os 2 últimos elemantos da lista [-2:] e adiciona ao final
        lista.append(sum(lista[-2:]))
    return lista


print(fibonacci(100))
print('\n\n\n\n')
for elemento in fibonacci(100):
    print(elemento)
