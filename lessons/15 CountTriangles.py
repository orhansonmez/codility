def solution_not_efficient(A):

    triangles, N = 0, len(A)

    for P in range(N-2):
        for Q in range(P+1, N-1):
            for R in range(Q+1, N):
                if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]:
                    triangles += 1

    return triangles
