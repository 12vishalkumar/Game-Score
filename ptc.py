import math
import os
import random
import re
import sys

# Complete the 'breakingRecords' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.

def breakingRecords(scores):
    # Write your code here
    H = L = scores[0]
    l = len(scores)
    c1 = c2 = 0
    for i in range(1, l):
        h = max(H, scores[i])
        if(H<scores[i]):
            c1 += 1
            H = h
        l = min(L, scores[i])
        if(L>scores[i]):
            c2 += 1
            L =l
    return (c1, c2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()