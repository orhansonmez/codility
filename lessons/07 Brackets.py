def solution(S):

    stack = []
    pairs = [('(', ')'), ('[', ']'), ('{', '}')]

    for x in S:
        if stack:
            prev = stack.pop()
        else:
            stack.append(x)
            continue

        if (prev, x) not in pairs:
            stack.append(prev)
            stack.append(x)

    return 1 * (not stack)
