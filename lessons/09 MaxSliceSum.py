def solution(A):

    max_slice, max_sum = -1e12, 0
    for a in A:
        max_sum = max(a, max_sum + a)
        max_slice = max(max_slice, max_sum)

    return max_slice
