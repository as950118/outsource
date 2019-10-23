#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'protectionTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY startingPos
#  2. INTEGER_ARRAY speed
#
import sys
INF = sys.maxsize
ret = 0
def protectionTime(startingPos, speed):
    # Write your code here


if __name__ == '__main__':

    startingPos_count = int(input().strip())

    startingPos = []

    for _ in range(startingPos_count):
        startingPos_item = int(input().strip())
        startingPos.append(startingPos_item)

    speed_count = int(input().strip())

    speed = []

    for _ in range(speed_count):
        speed_item = int(input().strip())
        speed.append(speed_item)

    result = protectionTime(startingPos, speed)

    print(str(result) + '\n')
