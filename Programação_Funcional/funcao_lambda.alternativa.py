compras = (
    {'quantidade': 2, 'preço': 10},
    {'quantidade': 3, 'preço': 20},
    {'quantidade': 5, 'preço': 14},

)

#  Substituindo a função lambda pela função abaixo


def calc_preco_total(compra):
    return compra['quantidade']*compra['preço']

# Usando uma única linha
#  def calc_preco_total(compra): return compra['quantidade']*compra['preço']


totais = tuple(map(calc_preco_total, compras))

print('Preços Totais', totais)
print('Total geral:', sum(totais))
