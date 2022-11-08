def solution(A):

    max_value = -1e12
    for a in A:
        max_value = max(max_value, a)

    if max_value <= 0:
        return max_value

    max_slice, max_sum = 0, 0
    for a in A:
        max_sum = max(0, max_sum + a)
        max_slice = max(max_slice, max_sum)

    return max_slice
