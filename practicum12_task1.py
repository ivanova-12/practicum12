def pownum(a: float, n: int) -> float:
    """Calculate the n-degree num a"""
    
    if n == 0:
        return 1
    elif n == 1:
        return a
    return pownum(a, n - 1) * a
