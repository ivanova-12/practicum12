def mod_number(a: int, b: int) -> int:
    """Calculate the remainder of the division a by b"""

    if a < b:
        return a
    return mod_number(a - b, b)









