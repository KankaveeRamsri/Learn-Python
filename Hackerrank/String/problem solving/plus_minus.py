#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_negative = 0
    count_zero = 0
    count_positive = 0
    
    for i in arr:
        if i < 0:
            count_negative += 1
        elif i == 0:
            count_zero += 1
        elif i > 0:
            count_positive += 1
    
    print("{:.6f}".format(count_positive/len(arr)))
    print("{:.6f}".format(count_negative/len(arr)))
    print("{:.6f}".format(count_zero/len(arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
