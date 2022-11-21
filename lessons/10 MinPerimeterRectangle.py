def solution(N):

    minimal_perimeter = None
    for i in range(1, N + 1):
        if N % i == 0:
            minimal_perimeter = 2 * (i + N // i)

        if i * i > N:
            break

    return minimal_perimeter
