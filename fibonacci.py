# Yep, a simple recursive fibonacci thing that does, stuff, idk it just work shut up

def fib(n, k, e=1):
    if k != 0:
        # n = 0, e = 1
        fib(n + e, k-1, n)
        print(n)
    else:
        print(n)
        return n
