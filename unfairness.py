
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/angry-children/problem



import math
import random
import re
import sys

# The minimum unfairness is can be found just by looking for the minimum difference between the first and the final
# element of all sublists.

def maxMin(k, arr):

    arr = sorted(arr)

    unfairs = [] # empty list in which storing all the unfairness values

    for j in range(len(arr)-k+1):

        unfairs.append(arr[j+k-1]-arr[j])


    return min(unfairs)



if __name__ == '__main__':

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(str(result))
