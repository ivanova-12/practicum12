def maxlist(a: list[int]) -> int:
    """Find the max number from the list a"""

    if len(a) == 1:
        return a[0]
    return max(a[0], maxlist(a[1:]))















