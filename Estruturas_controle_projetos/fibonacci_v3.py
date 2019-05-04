def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')

    while ultimo < limite:
        (penultimo, ultimo) = (ultimo, penultimo + ultimo)
        print(ultimo, end=',')


fibonacci(10000)
