
def gcd(m: int, n: int) -> int:
    if n == 0:
        return m
    else:
        r = m % n
        m = n
        n = r
        return gcd(m, n)


print(gcd(27, 9))
