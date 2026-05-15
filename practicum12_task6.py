def degree5(n: int) -> int:
    """Calculate what power of 5 a natural number n is"""

    if n == 1:
        return 0
    if n % 5 != 0:
        return -1
    result = degree5(n // 5)
    return -1 if result == -1 else result + 1







