def solution(H):

    stack = []
    stone_blocks = 0

    for h in H:
        if not stack:
            stone_blocks += 1
            stack.append(h)
            continue

        prev = 1e10
        while prev > h and stack:
            prev = stack.pop()

        if prev < h:
            stack.append(prev)

        stack.append(h)

        if prev != h:
            stone_blocks += 1

    return stone_blocks
