def solution_not_efficient(A):

    N = len(A)
    non_divisors = [0] * N

    for i in range(N):
        for j in range(N):
            if A[i] % A[j] > 0:
                non_divisors[i] += 1

    return non_divisors
