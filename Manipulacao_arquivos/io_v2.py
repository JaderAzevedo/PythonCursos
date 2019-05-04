# Abertura e leitura por stream
arquivo = open('pessoas.csv')

for registro in arquivo:
    # Atenção: Quebra na "," e extração dos dados com "*"
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

arquivo.close()
