def ind_maxlist(a: list[int]) -> int:
    """Find the index of max elem in a"""

    if not a:
        return -1
    if len(a) == 1:
        return 0
    ind = ind_maxlist(a[1:]) + 1
    if a[0] > a[ind]:
        return 0
    return ind

