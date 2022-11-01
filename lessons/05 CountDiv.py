def solution(A, B, K):

    minimum = int(A / K) + (A % K != 0)
    maximum = int(B / K)

    return maximum - minimum + 1
