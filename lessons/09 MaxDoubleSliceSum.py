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

def solution(A):

    N = len(A)
    forward = [0] * N
    backward = [0] * N

    for i in range(1, N - 2):
        forward[i + 1] = max(0, forward[i] + A[i])

    for i in range(N - 2, 1, -1):
        backward[i - 1] = max(0, backward[i] + A[i])

    max_sum = 0
    for i in range(1, N - 1):
        max_sum = max(max_sum, forward[i] + backward[i])

    return max_sum
