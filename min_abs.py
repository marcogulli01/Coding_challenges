
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

import math
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.

def minimumAbsoluteDifference(arr):

    n = len(arr)

    sortedarr = sorted(arr) # sort the array according to ascending order

    diff = [] # array in which differences between consecutive numbers will be stored

    for i in range(n-1):
        difference = abs(sortedarr[i+1] - sortedarr[i])
        diff.append(difference)

    return min(diff) 


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(minimumAbsoluteDifference(arr))

