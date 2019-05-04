# Abertura, cópia e fechamento do arquivo
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()


for registro in dados.splitlines():
    # Atenção: Quebra na "," e extração dos dados com "*"
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
