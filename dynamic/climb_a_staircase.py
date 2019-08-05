
def count_ways(n, X = [1, 2]):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    res = 0
    for step in X:
        res += count_ways(n-step)
    return res
