from math import pi


def circulo(raio):
    area_circulo = pi * raio**2
    return area_circulo


if __name__ == '__main__':
    raio = float(input('Informe o raio: '))
    area = circulo(raio)
    print('Área do círculo é', area)
