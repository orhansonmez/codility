def solution(A):

    value, size = None, 0
    for x in A:
        if size == 0:
            size += 1
            value = x
            continue

        if x == value:
            size += 1
        else:
            size -= 1

    # print(value, size)

    if size == 0:
        return 0

    N = len(A)
    size, leader = 0, None

    for k in range(N):
        if A[k] == value:
            size += 1

            if size > N // 2:
                leader = value
                break

    # print(leader)

    if leader is None:
        return 0

    prefix_sums = [0] * (N + 1)
    for k in range(N):
        prefix_sums[k + 1] = prefix_sums[k] + (A[k] == leader)

    # print(prefix_sums)

    equileaders = 0
    for S in range(N):
        left = prefix_sums[S + 1] - prefix_sums[0]
        right = prefix_sums[N] - prefix_sums[S + 1]

        # print(S, left, (S+1) // 2, right, (N - S - 1) // 2)

        if left > ((S + 1) // 2) and right > ((N - S - 1) // 2):
            equileaders += 1

    # print(equileaders)
    return equileaders
