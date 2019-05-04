# Abertura e leitura por stream
arquivo = open('pessoas.csv')

for registro in arquivo:
    # Atenção: Quebra na "," e extração dos dados com "*"
    # Strip : retira espaços em braco e \n,\t ,etc... das borda das strings

    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
