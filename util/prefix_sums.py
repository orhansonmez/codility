def calculate_prefix_sums(A):

    N = len(A)
    prefix_sums = [0] * (N+1)

    for i in range(N):
        prefix_sums[i+1] = prefix_sums[i] + A[i]

    return prefix_sums


def main():
    A = [1,5,7,8,2,3,12,67,98,234,2,6,275,23]
    print(A)

    prefix_sums = calculate_prefix_sums(A)
    print('Prefix Sums : ', prefix_sums)

    print('Sum of the elements between 3 and 7 (inclusive): ',
          'prefix_sum[7+1] - prefix_sum[3] = ',
          prefix_sums[7+1] - prefix_sums[3])


if __name__ == "__main__":
    main()