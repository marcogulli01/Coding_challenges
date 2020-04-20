
# Solution of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/permutation-equation/problem

# The solution of the problem can be implemented by carring out binary search twice

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.

n = int(input())

p = list(map(int, input().rstrip().split()))

inds = []

for i in range(n):
    for item in p:
        if item == (i+1):
            inds.append(p.index(item)+1)

inds2 = []

for item in inds:
    for number in p:
        if item == number:
            inds2.append(p.index(number)+1)

print('\n'.join(map(str,inds2)))

