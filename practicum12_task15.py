def ten_to_bin(x: int) -> str:
    """Calculate the binary form of a number"""

    result = ''
    if x == 0:
        return ''
    result += ten_to_bin(x // 2)
    result += str(x % 2)
    return result





