
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/beautiful-pairs/problem

import math
import random
import re
import sys

n = int(input().strip())  # size of A and B
A = [int(number) for number in input().strip().split(' ')]
B = [int(number) for number in input().strip().split(' ')]

# sort both arrays

A.sort()
B.sort()
a, b, counter = 0, 0, 0 # a and b are indices, counter is a variable

while a < n and b < n:
    if A[a] > B[b]: # if the element in A is larger than the correspondent one in B, increase b by 1
        b += 1
    elif A[a] < B[b]: # if the element in A is smaller than the correspondent one in B, increase a by 1
        a += 1
    else: # if the element in A is equal to the correspondent one in B, raise counter by 1 and go ahead with the indices
        counter += 1
        a += 1
        b += 1

if counter == n:
    print(n-1)  # one value must be changed
else:
    print(counter+1) 
