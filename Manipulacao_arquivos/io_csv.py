# Importando a classe para tratar csv
import csv
# Usando whith para garantir o fechamento do arquivo
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))
