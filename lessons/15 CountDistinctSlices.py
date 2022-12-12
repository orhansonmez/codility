def solution(M, A):

    head, tail = -1, 0
    distinct_slices = 0
    elements = set()

    while tail < len(A):

        head += 1
        if head >= len(A):
            break

        if A[head] in elements:
            while A[tail] != A[head]:
                elements.remove(A[tail])
                tail += 1
            tail += 1
        else:
            elements.add(A[head])

        distinct_slices += head - tail + 1

        if distinct_slices >= 1e9:
            return int(1e9)

    return distinct_slices
