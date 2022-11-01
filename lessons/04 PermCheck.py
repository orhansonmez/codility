def solution(A):

    elements = set()
    for x in A:
        elements.add(x)

    if len(elements) != len(A):
        return 0

    if max(A) != len(A):
        return 0

    return 1
