def solution(N):

    i = 1
    factor = 0

    while i ** 2 < N:
        if N % i == 0:
            factor += 2
        i += 1

    if i ** 2 == N:
        factor += 1

    return factor
