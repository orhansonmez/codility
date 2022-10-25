def solution(A):

    total = sum(A)

    current_sum = 0
    best_diff = float('inf')

    for x in A[:-1]:

        current_sum += x
        other_sum = total - current_sum

        diff = abs(other_sum - current_sum)
        if diff < best_diff:
            best_diff = diff

    return best_diff