
# Solution of the challenge Cut the Sticks proposed on HackerRank at https://www.hackerrank.com/challenges/cut-the-sticks/problem

import math
import random
import re
import sys


# A list called occ contains the occurrences of all non-dubplicate elements from arr sorted into ascending order.
# A list called recurr should start with len(arr) and go ahead with the difference between len(arr) and the first
# element of occ. Iterating this process until the difference recurr[i]-occ[i] = 0 will solve the problem.

def cutTheSticks(arr):

    occ = [arr.count(item) for item in sorted(list(set(arr)))]

    recurr = [len(arr)]

    for i in range(len(occ)):
        m = recurr[i]-occ[i]
        if m != 0:
            recurr.append(m)

    return recurr

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))


