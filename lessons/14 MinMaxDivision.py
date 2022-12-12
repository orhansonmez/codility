def solution(K, M, A):

    lower, upper = max(A), sum(A)
    result = -1

    while lower <= upper:

        candidate = (lower + upper) // 2

        block_count, current_sum = 0, 0
        for element in A:
            if current_sum + element <= candidate:
                current_sum += element
            else:
                current_sum = element
                block_count += 1
        block_count += 1

        if block_count > K:
            lower = candidate + 1
        else:
            upper = candidate - 1
            result = candidate

    return result
