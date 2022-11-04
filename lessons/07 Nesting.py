def solution(S):

    stack = []

    for x in S:
        if stack:
            prev = stack.pop()
        else:
            stack.append(x)
            continue

        if not (prev == '(' and x == ')'):
            stack.append(prev)
            stack.append(x)

    return 1 * (not stack)
