# Yet another fibonacci thing. I used mAtH to cheat a bit

from math import sqrt

PHI = (sqrt(5)+1)/2
l = []
def fib_II(n, k):
    n = int(n)
    k = int(k)
    # Yes, this is a jojo reference :)
    GOLDEN_WIND = round(n/PHI)
    fib_tail(n, k, GOLDEN_WIND)
    
    # Thanks for the feedback tamatoo :D
    return ','.join(map(str, l[1:]))

def fib_tail(n, k, e):
    if k != 0:
        # n = 0, e = 1
        l.append(n)
        fib_tail(n + e, k-1, n)     
    else:
        l.append(n)
        return n

