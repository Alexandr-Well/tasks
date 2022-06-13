import math
from typing import Optional


def quadratic_eq(a: float, b: float, c: float) -> Optional:
    """
    функция для решения квадратного уравнения
    :param a: float
    :param b: float
    :param c: float
    :return: float of str
    """
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        return round((-b + math.sqrt(discr)) / (2 * a), 2), round((-b - math.sqrt(discr)) / (2 * a), 2)
    elif discr == 0:
        return round(-b / (2 * a), 2),
    else:
        return "Корней нет"


if __name__ == '__main__':
    print(quadratic_eq(1, 2, 1))
