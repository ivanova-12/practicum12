def combin(n: int, k: int) -> int:
    """Calculate how much combination has this pair of numbers"""

    if k == 0:
        return 1
    if n < k:
        return 0
    if n == k:
        return 1
    if n > k and k == 1:
        return n
    return combin(n - 1, k - 1) + combin(n - 1, k)

print(combin(9, 2))













