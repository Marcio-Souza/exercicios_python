def contar_caracteres(s):
    """ Funcao que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s:
    :return:
    """
    resultado = {}
    s = sorted(s)

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('banana'))
    print()
    print(contar_caracteres('Mariana'))
