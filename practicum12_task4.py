def sum_progress(a1: float, r: float, n: int) -> float:
    """Calculate the sum of n-numbers of progression"""

    if n == 1:
        return a1
    return sum_progress(a1 + r, r, n - 1) + a1

