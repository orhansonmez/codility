from random import randint


def quicksort(A):

    if len(A) <= 1:
        return A

    smaller, same, bigger = [], [], []

    pivot = A[randint(0,len(A)-1)]

    for x in A:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            same.append(x)
        else:
            bigger.append(x)

    return quicksort(smaller) + same + quicksort(bigger)


def main():
    A = [1,5,7,8,2,3,12,67,98,234,2,6,275,23]
    print(A)
    print('QuickSorted : ', quicksort(A))


if __name__ == "__main__":
    main()