def count(n: int) -> int:
    """Calculate the count of all symbols in num"""
    
    if n < 10:
        return 1
    return count(n // 10) + count(n % 10)







