import sys
import math


def calc_hipotenusa(b, c):
    a = math.sqrt((b * b) + (c * c))
    return a


def calc_area_comprimento_circulo(r):
    a = math.pi * (r * r)
    c = 2 * math.pi * r
    return a, c


def calc_imc(h, m):
    imc = m / (h * h)
    return imc


def calc_distancia_2pontos(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    return d
