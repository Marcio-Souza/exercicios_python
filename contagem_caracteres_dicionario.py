def contar_caracteres(s):
    """ Funcao que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}
    :param s:
    :return:
    """
    caracter_ordenado = sorted(s)
    caracter_anterior = caracter_ordenado[0]
    contagem = 1
    resultado = {}

    for caracter in caracter_ordenado[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1
    resultado[caracter_anterior] = contagem
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('banana'))
    print()
    print(contar_caracteres('Mariana'))
