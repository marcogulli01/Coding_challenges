
# Solution of the challenge Ice Cream Parlor proposed on Hackerrank at https://www.hackerrank.com/challenges/missing-numbers/problem

import random
import re
import sys

# We should build a double for-loop over the array arr. As soon as the unique pair of indices has been found,
# the indices should be translated by 1 and then returned by the function

def icecreamParlor(m, arr):


    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == m:
                ind1 = i + 1
                ind2 = j + 1

    return [ind1, ind2]


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(result)


