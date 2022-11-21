def solution_not_efficient(A):

    N = len(A)
    if N < 3:
        return 0

    peaks = []
    for i in range(1, N - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)

    P = len(peaks)
    if not peaks:
        return 0

    diff = []
    for i in range(P - 1):
        diff.append(peaks[i + 1] - peaks[i])

    max_flags = 1
    for K in range(2, P + 1):

        if K * (K - 1) > sum(diff):
            break

        flags, distance = 1, 0
        for d in diff:
            if distance + d >= K:
                distance = 0
                flags += 1

                if flags >= K:
                    break
            else:
                distance += d

        if flags >= K:
            max_flags = K
        else:
            break

    return max_flags
