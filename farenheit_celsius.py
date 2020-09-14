"""
Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""


def farenheit_celsius(fare):
    f = fare
    celsius = 5 * (f -32) /9
    return celsius


if __name__ == '__main__':
    print(farenheit_celsius(77))
