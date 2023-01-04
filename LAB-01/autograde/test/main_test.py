import sys
import pytest
from faker import Faker
import math
import main

fake = Faker()


def test_calc_hipotenusa():
    cateto1 = fake.random_number()
    cateto2 = fake.random_number()

    actual = main.calc_hipotenusa(cateto1, cateto2)
    expected = math.hypot(cateto1, cateto2)

    assert actual == expected


def test_calc_area_comprimento_circulo():
    raio = fake.random_number()

    actual = main.calc_area_comprimento_circulo(raio)
    expected = math.pi * (raio ** 2), 2 * math.pi * raio

    assert actual == expected


def test_calc_imc():
    altura = fake.random_number()
    massa = fake.random_number()

    actual = main.calc_imc(altura, massa)
    expected = massa / (altura ** 2)

    assert actual == expected


def test_calc_distancia_2pontos():
    x1 = fake.random_number()
    x2 = fake.random_number()
    y1 = fake.random_number()
    y2 = fake.random_number()

    actual = main.calc_distancia_2pontos(x1, y1, x2, y2)
    expected = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    assert actual == expected
