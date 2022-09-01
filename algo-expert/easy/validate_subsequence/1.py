# easy, arrays
# time O(n) | space O(1)
def isValidSubsequence(array, sequence):
    len_seq = len(sequence)
    len_arr = len(array)
    p1 = 0
    p2 = 0
    while p1 < len_arr and p2 < len_seq:
        if array[p1] == sequence[p2]:
            p2 += 1
        p1 += 1
    return p2 == len_seq
