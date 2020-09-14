"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.

F = (C × 9/5) + 32
"""


def celsius_farenheit(celsius):
    """
    >>> celsius_farenheit(25)
    77.0

    :param celsius: Integer
    :return:
    """
    c = celsius
    farenheit = (c * 9 / 5) + 32
    return farenheit


if __name__ == '__main__':
    print(celsius_farenheit(25))
