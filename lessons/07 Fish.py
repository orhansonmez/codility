def solution(A, B):

    stack = []

    for i in range(len(A)):
        fish = (A[i], B[i])

        if stack:
            upstream = stack.pop()
        else:
            stack.append(fish)
            continue

        if fish[1] == 1 or upstream[1] == 0:
            stack.append(upstream)
            stack.append(fish)
            continue

        while upstream[1] == 1 and fish[0] > upstream[0]:
            if stack:
                upstream = stack.pop()
            else:
                upstream = None
                stack.append(fish)
                break

        if upstream:
            if upstream[1] == 1 and fish[0] < upstream[0]:
                stack.append(upstream)
            if upstream[1] == 0:
                stack.append(upstream)
                stack.append(fish)

    return len(stack)
