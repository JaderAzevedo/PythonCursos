def imprimir(atual, maximo):
    if atual < maximo:
        print(atual)
        imprimir(atual+1, maximo,)


imprimir(1, 100)
