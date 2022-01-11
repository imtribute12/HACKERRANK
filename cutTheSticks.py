#!/bin/python3
import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    counter = []
    i = 0
    while len(arr) > 0 : 
        minimum = min(arr)
        length = len(arr)
        counter.append(length)
        
        for y in range(length):
            arr[y] = arr[y] - minimum
        
        for x in range(arr.count(0)):
            arr.remove(0)  
           
    
    return [counter[j] for j in range(len(counter))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
