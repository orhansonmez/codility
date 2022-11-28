def calculate_gcd(x, y):
    if y > x:
        x, y = y, x

    if x % y == 0:
        return y
    return calculate_gcd(x % y, y)


def same_prime_divisors(x, y):
    gcd = calculate_gcd(x, y)

    while x > 1:
        step_gcd = calculate_gcd(x, gcd)
        if step_gcd == 1:
            return 0
        x /= step_gcd

    while y > 1:
        step_gcd = calculate_gcd(y, gcd)
        if step_gcd == 1:
            return 0
        y /= step_gcd

    return 1


def solution(A, B):
    count = 0
    for a, b in zip(A, B):
        count += same_prime_divisors(a, b)

    return count
