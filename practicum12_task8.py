def fib(k: int) -> int:
    """Calculate the k-th number of fibonacci numbers"""

    if k == 1 or k == 2:
        return 1
    return fib(k - 1) + fib(k - 2)

