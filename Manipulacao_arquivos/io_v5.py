# Usando whith para garantir o fechamento do arquivo
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        # Atenção: Quebra na "," e extração dos dados com "*"
        # Strip : retira espaços em braco e \n,\t ,etc... das borda das strings

        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
if arquivo.closed:
    print('Arquivo Fechado!')
