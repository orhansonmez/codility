def solution(S):

    stack = []
    pairs = [('(', ')'), ('[', ']'), ('{', '}')]

    for x in S:
        prev = None
        if stack:
            prev = stack.pop()

        if (prev, x) not in pairs:
            if prev:
                stack.append(prev)
            stack.append(x)

    return 1 * (not stack)
