
# Solution of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/picking-numbers/problem

import math
import random
import re
import sys

# read the input from terminal

n = int(input().strip())
a = list(map(int,input().strip().split(' ')))

maximum = 0 # initialize the maximum at 0

for k in list(set(a)): # loop over the single elements of a list with no duplicates
    n1 = a.count(k) # number of occurrences of the element k in the list
    n2 = a.count(k-1) # number of the occurrences of the element k-1 in the list
    maximum = max(maximum, n1+n2) # maximum between the maximum calculated at the previous step and n1 + n2

print(maximum)


