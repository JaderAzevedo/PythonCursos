from math import pi
import sys

ERRO = '\033[91m'  # Mudar para a cor vermelha  NÃO ESTÁ FUNCIONANDO NO WINDOWS
NORMAL = '\033[0m'  # Mudar para a cor normal   NÃO ESTÁ FUNCIONANDO NO WINDOWS


def circulo(raio):
    area_circulo = pi * raio**2
    return area_circulo


def help():
    print(f""" 
    É necessário informar o raio do círculo.
    Sintaxe: {sys.argv[0][-20:]} <raio> """)


if __name__ == '__main__':
    # Pegando o valor diretamente da linha de comando
    if len(sys.argv) < 2:
        help()
        sys.exit(1)  # Sai do programa e informa o status "1" (com erro)
    elif not sys.argv[1].isnumeric():
        help()
        print(ERRO, '    O raio deve ser numérico \n \n', NORMAL)
    else:
        raio = float(sys.argv[1])
        area = circulo(raio)
        print('Área do círculo é', area)
