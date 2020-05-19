

# Solution of the challenge Pairs proposed on HackerRank at https://www.hackerrank.com/challenges/pairs/problem

import math
import random
import re
import sys

# Given the array arr, we should add the target value k to each of its elements, so that we get a new array called
# sum_set. After converting both arr and sum_set to sets, the answer is the length of the intersection between
# the two sets. 


def pairs(k, arr):

    sum_set = set(item + k for item in arr)

    return len(set.intersection(set(arr), sum_set))


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)





