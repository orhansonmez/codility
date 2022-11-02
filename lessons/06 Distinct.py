def solution(A):

    if not A:
        return 0

    A.sort()

    unique = 1
    for i in range(len(A) - 1):
        if A[i] != A[i + 1]:
            unique += 1

    return unique
