class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    # Tornando a class interável
    def __next__(self):
        try:
            # Retire o último elemento da lista 'pop'
            return self.cores.pop()
        except IndexError:
            # Se a lista estiver vazio pare a interação
            raise StopIteration()

    # Para poder utilizar em laços for,etc...

    def __iter__(self):
        return self


cores = RGB()
print(next(cores))
print(next(cores))
print(next(cores))


#  Só é possível devedo ao médoto __iter__
for cor in RGB():
    print(cor)
