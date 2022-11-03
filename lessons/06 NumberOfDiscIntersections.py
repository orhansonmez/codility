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


def solution(A):

    events = []
    for i in range((len(A))):
        events += [(i - A[i], 1), (i + A[i], -1)]
    events.sort(key=lambda e: (e[0], -e[1]))

    intersections, active_circles = 0, 0
    for _, event in events:
        intersections += active_circles * (event > 0)
        active_circles += event

        if intersections > 10E6:
            return -1

    return intersections
