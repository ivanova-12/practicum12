def helping(x: int, n: int) -> str:
    """Сonverts a natural number x (not including zero)
    from the decimal number system
    to the n-ary number system
    """

    digits = '0123456789ABCDEF'
    result = ''
    if x == 0:
        return ''
    result += helping((x // n), n)
    result += digits[x % n]
    return result


def ten_to_n(x: int, n: int) -> str:
    """Сonverts a natural number x (including zero)
    from the decimal number system
    to the n-ary number system """

    if x == 0:
        return '0'
    return helping(x, n)

