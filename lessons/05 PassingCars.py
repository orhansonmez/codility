def solution(A):

    N = len(A)
    suffix_sums = [0] * N

    suffix_sums[N - 1] = A[N - 1]
    for i in range(1, N):
        suffix_sums[N - i - 1] = A[N - i - 1] + suffix_sums[N - i]

    passing_cars = 0

    for i in range(len(A)):

        if A[i] == 0:
            passing_cars += suffix_sums[i]

            if passing_cars > 1000000000:
                return -1

    return passing_cars
