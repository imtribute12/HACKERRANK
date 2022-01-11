#!/bin/python3

import math
import os
import random
import re
import sys

def permutationEquation(p):
    arr = []
    for y in range(1,len(p)+1):
        arr.append(p.index(p.index(y)+1)+1)
    return [arr[i] for i in range(len(arr))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
