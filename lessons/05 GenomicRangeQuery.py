def solution(S, P, Q):

    values = dict()
    values['A'] = 10 ** 12
    values['C'] = 10 ** 6
    values['G'] = 1
    values['T'] = 0

    prefix_sums = [0] * (len(S) + 1)
    for i in range(len(S)):
        prefix_sums[i + 1] = values[S[i]] + prefix_sums[i]

    output = []
    for K in range(len(P)):

        diff = prefix_sums[Q[K] + 1] - prefix_sums[P[K]]

        min_impact_factor = 4
        if diff >= 10 ** 12:
            min_impact_factor = 1
        elif diff >= 10 ** 6:
            min_impact_factor = 2
        elif diff > 0:
            min_impact_factor = 3

        output += [min_impact_factor]

    return output
