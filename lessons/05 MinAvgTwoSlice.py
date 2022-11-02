def solution_not_efficient(A):

    N = len(A)

    prefix_sums = [0] * (N + 1)
    for i in range(N):
        prefix_sums[i + 1] = prefix_sums[i] + A[i]

    min_avg = 10001
    min_avg_index = -1

    for q in range(1, N):
        for p in range(0, q):
            avg = (prefix_sums[q + 1] - prefix_sums[p]) / (q - p + 1)

            if avg < min_avg:
                min_avg = avg
                min_avg_index = p

    return min_avg_index
