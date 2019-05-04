# Usando whith para garantir o fechamento do arquivo
with open('pessoas.csv') as arquivo:
    # Usando w para escrever no arquivo
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            # Atenção: Quebra na "," e extração dos dados com "*"
            # Strip : retira espaços em braco e \n,\t ,etc...
            # das borda das strings
            pessoa = registro.strip().split(',')
            # Print no arquivo de saida
            print('Nome: {}, \t\tIdade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo Fechado!')

if saida.closed:
    print('Saida Fechado!')
