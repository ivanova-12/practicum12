def numbers(x: int) -> None:
    """Print the digits of a natural number x in reverse order"""
    
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)

