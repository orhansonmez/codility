def solution(A):

    absolute_distinct_values = set()

    for x in A:
        absolute_distinct_values.add(abs(x))

    return len(absolute_distinct_values)
