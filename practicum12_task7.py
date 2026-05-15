def nod(a: int, b: int) -> int:
    """Calculate the biggest num which can divide by a and b"""
    
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    return nod(max(a, b) % min(a, b), min(a, b))

