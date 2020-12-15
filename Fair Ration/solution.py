#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.


def fairRations(b):
    try:
        count = 0
        for a, i in enumerate(b):
            if i % 2 != 0:
                temp1 = b[a]
                temp2 = b[a+1]
                b.pop(a+1)
                b.pop(a)
                b.insert(a, temp1+1)
                b.insert(a+1, temp2+1)
                count += 1
        return 2*count
    except:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
