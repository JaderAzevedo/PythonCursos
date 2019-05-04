from math import pi
import sys


def circulo(raio):
    area_circulo = pi * raio**2
    return area_circulo


def help():
    print(f""" 
    É necessário informar o raio do círculo.
    Sintaxe: {sys.argv[0][-20:]} <raio> \n """)


if __name__ == '__main__':
    # Pegando o valor diretamente da linha de comando
    if len(sys.argv) < 2:
        help()
    else:
        raio = float(sys.argv[1])
        area = circulo(raio)
        print('Área do círculo é', area)
