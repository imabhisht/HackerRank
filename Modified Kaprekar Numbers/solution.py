#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.


def kaprekarNumbers(p, q):
    xamp = []
    found = False
    for i in range(p, q+1, 1):
        if i == 1:
            xamp.append(i)
            found = True
        elif len(str((i)*(i))) >= 2:
            leni = len(str(i))
            split_l1 = str((i)*(i))[:leni]
            split_r1 = str((i)*(i))[leni:]
            split_l2 = str((i)*(i))[:-leni]
            split_r2 = str((i)*(i))[-leni:]
            if i == (int(split_l1) + int(split_r1)):
                if int(split_r1) == 0:
                    pass
                else:
                    xamp.append(i)
                    found = True
            elif i == (int(split_l2) + int(split_r2)):
                if int(split_r1) == 0:
                    pass
                else:
                    xamp.append(i)
                    found = True

    if found == False:
        print('INVALID RANGE')
    else:
        print(*xamp)


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
