def solution(X, A):

    if len(A) < X:
        return -1

    time = -1

    leaves = set()
    for t, leaf in enumerate(A):
        leaves.add(leaf)

        if len(leaves) == X:
            time = t
            break

    return time
