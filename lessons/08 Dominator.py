def solution(A):

    value, size = None, 0
    for x in A:
        if size == 0:
            size += 1
            value = x
            continue

        if value == x:
            size += 1
        else:
            size -= 1

    if size == 0:
        return -1

    size = 0
    for k in range(len(A)):
        if A[k] == value:
            size += 1

            if size > len(A) // 2:
                return k
    return -1
