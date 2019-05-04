def fibonacci(limite):
    lista = [0, 1]
    while lista[-1] < limite:
        lista.append(lista[-1]+lista[-2])
    return lista


print(fibonacci(10000))
print('\n\n\n\n')
for elemento in fibonacci(10000):
    print(elemento)
