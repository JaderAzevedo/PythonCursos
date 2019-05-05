compras = (
    {'quantidade': 2, 'preço': 10},
    {'quantidade': 3, 'preço': 20},
    {'quantidade': 5, 'preço': 14},

)
# Usando list e em uma única linha
totais=list(map(lambda compra: compra['quantidade']*compra['preço'], compras))

# totais = list(
#     map(
#         lambda compra: compra['quantidade']*compra['preço'],
#         compras
#     )
# )

print('Preços Totais', totais)
print('Total geral:', sum(totais))
