def binary_search(A, x):

    N = len(A)
    begin, end = 0, N-1
    result = -1

    while begin <= end:

        mid = (begin + end) // 2

        if A[mid] == x:
            result = mid
            break

        if A[mid] < x:
            begin = mid + 1
        else:
            end = mid - 1

    print(result)


def main():

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]

    binary_search(A, 7)
    binary_search(A, 99)


if __name__ == '__main__':
    main()
