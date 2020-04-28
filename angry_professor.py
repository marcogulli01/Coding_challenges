
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/angry-professor/problem



import math
import random
import re
import sys

# To solve this problem, we should count how many elements from the array a are larger than the threshold k 

def angryProfessor(k, a):

    ontime = 0

    for i in range(len(a)):
        if a[i] <= 0:
            ontime += 1

    if ontime >= k:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)
