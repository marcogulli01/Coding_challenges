
# Solution of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/maximizing-xor/problem

import math
import random
import re
import sys

# In order to find the maximum value of xor between two numbers, we should build a double for loop that could allow
# us to store the result of the XOR operation between any two numbers

def maximizingXor(l, r):

    xors = []

    for i in range(l,r+1):
        for j in range(r+1-i):
            xors.append(i^(i+j))

    return max(xors)


if __name__ == '__main__':

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    print(result)

