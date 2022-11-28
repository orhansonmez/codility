def solution(A, B):

    max_A, max_B = max(A), max(B)

    if max_A == 1:
        return [1] * len(A)

    ways = [0] * max_A

    ways[0], ways[1] = 1, 2
    for i in range(2, max_A):
        ways[i] = (ways[i - 1] + ways[i - 2]) % (2 ** max_B)

    output = []
    for a, b in zip(A, B):
        output.append(ways[a - 1] % (2 ** b))

    return output
