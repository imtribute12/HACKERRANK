#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    
    count = 0
    x = 0 
    
    while x < len(c)-1:
        if(c[x] == 0):
            if(x + 2 < len(c) and c[x+2] == 0):
                count = count+1
                x = x + 2
            elif(x + 1 < len(c) and c[x+1] == 0):
                count = count+1
                x = x + 1
        else:
            x = x + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
