import os
import random
import re
import sys

def biggerIsGreater(w):
    words = list(w)
    
    i = j = length = len(words) - 1
    
    while i > 0 and words[i - 1] >= words[i]:
        i -= 1
    
    if i<=0:
        return "no answer"
    while words[j] <= words[i - 1]:
        j -= 1
        
    words[i - 1], words[j] = words[j], words[i - 1]

    words[i:] = words[length:i - 1:-1]
    
    return ''.join(words)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close() 
