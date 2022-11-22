def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def lcm(x, y):
    if x > y:
        return x * y // gcd(x, y)
    else:
        return x * y // gcd(y, x)


def solution(N, M):
    return lcm(N,M) // M
