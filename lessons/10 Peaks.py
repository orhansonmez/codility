def solution_probably_buggy(A):

    N = len(A)
    peaks = [False] * N

    peak_count = 0
    for i in range(1, N - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks[i] = True
            peak_count += 1

    maximum_block_count = 0

    for i in range(1, peak_count + 1):
        if N % i == 0:

            block_count = i
            block_size = N // i

            peak_in_all_blocks = True

            for x in range(block_count):

                peak_in_the_block = False

                for y in range(block_size):
                    peak_in_the_block = peak_in_the_block or A[x * block_size + y]

                    if peak_in_the_block:
                        break

                peak_in_all_blocks = peak_in_all_blocks and peak_in_the_block

                if not peak_in_all_blocks:
                    break

            if peak_in_all_blocks:
                maximum_block_count = block_count

    return maximum_block_count