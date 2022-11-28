def solution(A):

    N = len(A)

    F, x = [0, 1], 0
    while x <= N + 1:
        x = F[-1] + F[-2]
        F.append(x)
    F.pop()

    reachable = [False] * (N + 2)
    jumps = [-1] * (N + 2)

    A = [1] + A + [1]
    reachable[0], jumps[0] = True, 0

    for i in range(1, N + 2):
        if A[i] == 0:
            continue

        for f in reversed(F[1:]):
            if i - f >= 0 and reachable[i - f] == True:
                reachable[i] = True

                if jumps[i] == -1 or jumps[i - f] + 1 < jumps[i]:
                    jumps[i] = jumps[i - f] + 1

    if reachable[N + 1]:
        return jumps[N + 1]
    else:
        return -1
