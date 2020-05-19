
# Solution of the challenge Jumping on Clouds: revisited proposed on HackerRank at https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

import math
import random
import re
import sys

# In order to find the cumulative number of points lost, we should first check whether the length of c is a
# multiple of k. If this happens, we just retain c. Otherwise, we would need to append to c a number of its copies
# equal to k-1. This array is named c_long. Next, starting from the first element, we should make jumps on the
# next clouds with a step size equal to k until completion. If we end up on 0, we should lower count by 1,
# if we end up on 1, we should lower count by 3.

def jumpingOnClouds(c, k):

    if len(c)%k == 0:
        c_long = c
    else:
        c_long = c*k
    
    count = 100 # initial score 

    for i in range(0,len(c_long),k):
        if c_long[i] == 0:
            count -= 1
        else:
            count -= 3

    return count


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)




