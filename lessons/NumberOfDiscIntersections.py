def solution_not_efficient(A):

    N = len(A)

    left, right = [], []
    for i in range(N):
        left.append(i - A[i])
        right.append(i + A[i])

    intersections = 0
    for i in range(N):
        for j in range(i + 1, N):
            if not (left[i] > right[j]) \
                    and not (right[i] < left[j]):
                intersections += 1

    return intersections
