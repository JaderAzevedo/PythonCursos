from math import pi
import sys


def circulo(raio):
    area_circulo = pi * raio**2
    return area_circulo


if __name__ == '__main__':
    # Pegando o valor diretamente da linha de comando
    raio = float(sys.argv[1])
    area = circulo(raio)
    print('Área do círculo é', area)
