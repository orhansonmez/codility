def solution(A):

    numbers = [False] * len(A)

    for x in A:
        if 0 < x <= len(A):
            numbers[x-1] = True

    for i in range(len(numbers)):
        if not numbers[i]:
            return i+1

    return len(A) + 1
