def gcd_with_division(a, b):
    if a % b == 0:
        return b
    return gcd_with_division(b, a % b)


def gcd(a, b, res):
    if a == b:
        return a * res
    if a % 2 == 0 and b % 2 == 0:
        return gcd(a // 2, b // 2, 2 * res)
    if a % 2 == 0:
        return gcd(a // 2, b, res)
    if b % 2 == 0:
        return gcd(a, b // 2, res)
    if a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)


def lcm(a, b):
    return a * b // gcd(a, b, 1)


def main():
    print(gcd_with_division(7250, 2500))
    print(gcd(7250, 2500, 1))
    print(lcm(12, 30))


if __name__ == '__main__':
    main()
