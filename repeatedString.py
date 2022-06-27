import os
import re
import sys

def repeatedString(s, n):
    
    return s[:n % len(s)].count("a") + s.count("a") * int(n / len(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    n = int(input().strip())
    
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()
