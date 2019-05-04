# Versão com generator

# Gera os dados sob medanda, utilizando muito memos memória
# (expressão  for item in list if condição)

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
