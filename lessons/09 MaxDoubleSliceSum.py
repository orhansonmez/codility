def solution_not_efficient(A):

    N = len(A)

    prefix_sums = [0] * (N + 1)
    for i in range(N):
        prefix_sums[i + 1] = prefix_sums[i] + A[i]

    max_double_slice = -1e12
    for X in range(len(A)):
        for Y in range(X + 1, len(A)):
            for Z in range(Y + 1, len(A)):
                double_slice = prefix_sums[Z] - prefix_sums[X + 1] - A[Y]

                if double_slice > max_double_slice:
                    max_double_slice = double_slice

    return max_double_slice
