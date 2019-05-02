#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTimes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY time
#  2. INTEGER_ARRAY direction
#
from collections import deque


def getTimes(time, direction):
    # Write your code here

    # time이 순서대로 들어오므로 따로 sort하지않았음
    que = deque()
    for i in range(time_count):
        que.append((time[i], direction[i], i))
    ret = [-1 for i in range(time_count)]
    flag = 1
    dif = 0
    prv_time, prv_dir, prv_i = que.popleft()
    cur_time, cur_dir, cur_i = prv_time, prv_dir, prv_i
    while que:
        cur_time, cur_dir, cur_i = que.popleft()
        if prv_time == cur_time:
            if prv_dir == flag:
                if ret[prv_i] != -1:

                else:
                    ret[prv_i] = prv_time
                    prv_time, prv_dir, prv_i = cur_time + 1, cur_dir, cur_i
            else:
                ret[cur_i] = cur_time
                prv_time += 1
            dif += 1
        else:
            ret[prv_i] = prv_time
            if prv_time + 1 == cur_time:
                flag = prv_dir
            else:
                flag = 1
            prv_time, prv_dir, prv_i = cur_time, cur_dir, cur_i
            dif = 0
        ret[prv_i] = prv_time
        ret[cur_i] = cur_time

    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    time_count = int(input().strip())

    time = []

    for _ in range(time_count):
        time_item = int(input().strip())
        time.append(time_item)

    direction_count = int(input().strip())

    direction = []

    for _ in range(direction_count):
        direction_item = int(input().strip())
        direction.append(direction_item)

    result = getTimes(time, direction)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
