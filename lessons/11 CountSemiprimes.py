def solution_not_efficient(N, P, Q):

    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    i = 2
    while i * i <= N:
        j = i * i
        while j <= N:
            is_prime[j] = False
            j += i
        i += 1

    primes = []
    for i, is_p in enumerate(is_prime):
        if is_p:
            primes.append(i)

    is_semiprime = [0] * (N + 1)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] <= N:
                is_semiprime[primes[i] * primes[j]] = 1

    prefix_sums = [0] * (N + 2)
    for i in range(1, N + 1):
        prefix_sums[i + 1] = prefix_sums[i] + is_semiprime[i]

    output = []
    for p, q in zip(P, Q):
        output.append(prefix_sums[q + 1] - prefix_sums[p])

    return output
