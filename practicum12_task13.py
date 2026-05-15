def odd_list(a: list[int], n: int) -> list[int]:
    """Return the list of even values in a"""

    if n == 0:
        return []
    result = odd_list(a[1:], n - 1)
    if a[0] % 2 == 0:
        return [a[0]] + result
    return result

