def solution(A):

    A_diff = [0] * len(A)

    for i in range(1, len(A)):
        A_diff[i] = A[i] - A[i - 1]

    max_slice, max_diff = 0, 0
    for a in A_diff:
        max_diff = max(0, max_diff + a)
        max_slice = max(max_slice, max_diff)

    return max_slice
