#!/bin/python3

import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    max = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in range(len(word)):
        letter = alphabet.index(word[i])
        
        if(h[letter]>max):
            max = h[letter]
            
    return len(word)*max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
