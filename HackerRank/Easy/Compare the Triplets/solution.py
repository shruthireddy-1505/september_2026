# HackerRank Problem: Compare the Triplets
# Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Difficulty: Easy
# Language: python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    ap = 0
    bp = 0
    i = 0
    j = 0
    while i < len(a) and j <len(b):
        if a[i] > b[i]:
            ap += 1
        elif b[i] > a[i]:
            bp += 1
        i +=1
        j += 1
    return [ap,bp]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
