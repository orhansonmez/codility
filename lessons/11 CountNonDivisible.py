def solution_not_efficient(A):

    N = len(A)
    non_divisors = [0] * N

    for i in range(N):
        for j in range(N):
            if A[i] % A[j] > 0:
                non_divisors[i] += 1

    return non_divisors


def solution(A):

    N = len(A)
    max_value = max(A)

    counts = [0] * (max_value + 1)
    for a in A:
        counts[a] += 1

    non_divisors = [N] * (max_value + 1)

    for i in range(1, max_value + 1):
        j = i
        while j <= max_value:
            non_divisors[j] -= counts[i]
            j += i

    output = []
    for a in A:
        output.append(non_divisors[a])

    return output
