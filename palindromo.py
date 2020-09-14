def palindrome(str):
    """
    Programa para verificar se uma string é um palindromo

    >>> palindrome('racecar')
    True

    :param str:
    :return:
    """
    lower = str.lower()
    for i in range(len(str) // 2):
        if lower[i] != lower[-i -1]:
            return False
        return True


if __name__ == '__main__':
    print(palindrome('racecar'))
