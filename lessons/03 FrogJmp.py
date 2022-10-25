def solution(X, Y, D):

    return int((Y - X) / D) + (((Y - X) % D) > 0) * 1
