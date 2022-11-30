def solution(A, B, C):

    planks = []
    for x in zip(A, B):
        planks.append(x)
    planks.sort(key=lambda x: (x[0], x[1]))

    N = len(planks)
    is_nailed = [False] * N

    for n, nail in enumerate(C):

        N = len(planks)
        begin, end = 0, N - 1

        result = -1
        while begin <= end:

            mid = (begin + end) // 2

            if planks[mid][0] <= nail <= planks[mid][1]:
                result = mid
                break

            if planks[mid][1] < nail:
                begin = mid + 1
            else:
                end = mid - 1

        if result == -1:
            continue

        planks_to_be_removed = []

        for i in range(result, N):
            if planks[i][0] <= nail <= planks[i][1]:
                planks_to_be_removed.append(i)
                is_nailed[i] = True

            if planks[i][0] > nail:
                break

        for i in range(result - 1, -1, -1):
            if planks[i][0] <= nail <= planks[i][1]:
                planks_to_be_removed.append(i)
                is_nailed[i] = True
            else:
                break

        all_nailed = True
        for nailed in is_nailed:
            if not nailed:
                all_nailed = False
                break

        if all_nailed:
            return n + 1

        planks_to_be_removed.sort(reverse=True)
        for i in planks_to_be_removed:
            del planks[i]
            del is_nailed[i]

    return -1
