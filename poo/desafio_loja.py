from datetime import datetime
from loja import Cliente,Vendedor,Compra

def main():
    cliente=Cliente('Maria Lima',44)
    vendedor= Vendedor('Pedro Garrido',36,5000)
    compra1=Compra(cliente,datetime.now,512)
    compra2=Compra(cliente,datetime(2019,6,4),256)

    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f'Cliente: {cliente}','(adulto)' if cliente.is_adulto else ' ')
    print(f'Vendedor: {vendedor}')

    valor_total= cliente.total_compras()
    qtde_item=len(cliente.compras)
    print(f'Total: {valor_total} em {qtde_item} itens')
    print(f' Última compra{cliente.get_data_ultima_compra()}')


main()