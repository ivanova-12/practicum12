def count(a: int, b: int) -> int:
    """Calculate hоw much squares you can cut off from the rectangle"""

    if a == 0 or b == 0:
        return 0
    if a == b:
        return 1
    if a < b:
        return (b // a) + count(a, b % a)
    return (a // b) + count(a % b, b)

