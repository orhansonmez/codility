def get_primes_till(N):

    primes = [True] * (N+1)
    primes[0] = primes[1] = False

    i = 2
    while i * i <= N:
        j = i * i
        while j <= N:
            primes[j] = False
            j += i
        i += 1

    return primes


def get_factors_till(N):

    factors_map = [0] * (N+1)

    i = 2
    while i * i <= N:
        j = i * i
        while j <= N:
            if factors_map[j] == 0:
                factors_map[j] = i
            j += i
        i += 1

    return factors_map


def get_factors_of(N):

    factors_map = get_factors_till(N)

    factors, i = [], N
    while factors_map[i] != 0:
        factors.append(factors_map[i])
        i = i // factors_map[i]
    factors.append(i)

    return factors


def main():
    primes = get_primes_till(72)
    for i in range(len(primes)):
        if primes[i]:
            print(i)

    factors = get_factors_of(354)
    print(factors)


if __name__ == '__main__':
    main()