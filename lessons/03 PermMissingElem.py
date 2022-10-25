def solution(A):

    N = len(A) + 1

    return int((N * (N + 1)) / 2) - sum(A)
