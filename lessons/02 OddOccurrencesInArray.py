def solution(A):

    elements = set()

    for x in A:
        if x in elements:
            elements.remove(x)
        else:
            elements.add(x)

    return elements.pop()


def solution_xor(A):

    value = 0
    for x in A:
        value ^= x

    return value
