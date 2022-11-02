def solution(A):

    A.sort()

    all_positives = A[-1] * A[-2] * A[-3]

    two_negatives = A[0] * A[1] * A[-1]

    if all_positives > two_negatives:
        return all_positives
    else:
        return two_negatives
