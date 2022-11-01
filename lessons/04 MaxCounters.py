def solution(N, A):

    values = [0] * N

    current_max = 0
    last_update = 0

    for op in A:
        if op <= N:
            if values[op - 1] < last_update:
                values[op - 1] = last_update + 1
            else:
                values[op - 1] += 1

            if values[op - 1] > current_max:
                current_max = values[op - 1]

        else:
            last_update = current_max

    for i in range(len(values)):
        if values[i] < last_update:
            values[i] = last_update

    return values
