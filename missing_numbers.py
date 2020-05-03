
# Solution of the challenge Missing Numbers proposed on Hackerrank at https://www.hackerrank.com/challenges/missing-numbers/problem


import math
import random
import re
import sys

# First, we need to get each element of brr only once, so we build a list called brrset containing all elements of brr without duplicates.
# For each element of brrset, we should first find the number of occurrences of the same element in arr and brr and append this number to a new pair of lists.
# After calculating the difference between the two lists and storing them into a list called diffs, for each non-zero element of diffs we should
# retrieve the index of the corresponding element in brrset

def missingNumbers(arr, brr):

    brrset = list(set(brr))

    occ_arr, occ_brr = [], []

    for item in brrset:
        occ_arr.append(arr.count(item))
        occ_brr.append(brr.count(item))

    diffs = []

    for i in range(len(occ_arr)):
        diffs.append(occ_brr[i]-occ_arr[i])

    missing = []

    for i in range(len(diffs)):
        if diffs[i] != 0:
            missing.append(brrset[i])

    return missing



if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))
