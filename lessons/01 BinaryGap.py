def solution(N):

    binary = "{0:b}".format(N)

    current_gap = 0
    maximum_gap = 0

    for b in binary[1:]:

        if b == '0':
            current_gap += 1

        if b == '1':
            if current_gap > maximum_gap:
                maximum_gap = current_gap
            current_gap = 0

    return maximum_gap
