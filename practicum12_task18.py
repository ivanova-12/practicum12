def simmetr(s: str, i: int, j: int) -> bool:
    """Determines whether the part of the string s
    starting from the i-th char and ending with the j-th char
    is symmetric
    """

    if i >= j:
        return True
    if s[i] == s[j]:
        return simmetr(s, i + 1, j - 1)
    else:
        return False

