def prime(x: int, n=2) -> int:
    """Check if x is a prime number using divisor n"""

    if x % n == 0 and x != n:
        return 0
    if n * n > x:
        return 1
    return prime(x, n + 1)

def function1(x: int) -> int:
    """Check if x is a prime number"""

    if x == 0 or x == 1:
        return 0
    return prime(x)

