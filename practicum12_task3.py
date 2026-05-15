def progress(a1: float, r: float, n: int) -> float:
    """Сalculate the n-th term of an arithmetic progression"""

    if n == 1:
        return a1
    return progress(a1 + r, r,  n - 1)













