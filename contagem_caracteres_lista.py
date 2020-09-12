def contar_caracteres(s):
    """ Funcao que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser retornada
    :return:
    """
    caracter_ordenado = sorted(s)
    caracter_anterior = caracter_ordenado[0]
    contagem = 1

    for caracter in caracter_ordenado[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('banana')
   # print()
   # contar_caracteres('Mariana')

