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
    que = [[] for i in range(200001)]
    for i in range(time_count):
        que[time[i]].append((direction[i], i))
    ret = [-1 for i in range(200001)]
    flag = 1
    for t in range(200001):
        if not que[t]:
            flag = 1
            continue
        temp_dir, temp_idx = [], []
        for d, i in que[t]:
            temp_dir.append(d)
            temp_idx.append(i)
        if len(temp_dir) == 1:
            ret[temp_idx[0]] = t
            flag = temp_dir[0]
            continue
        if len(temp_dir) == 2:
            dir0 = [temp_dir[0], temp_idx[0]]
            dir1 = [temp_dir[1], temp_idx[1]]
            if dir0[0] == flag:
                ret[dir0[1]] = t
                que[t + 1].append((dir1[0], dir1[1]))
                flag = dir0[0]
            else:
                ret[dir1[1]] = t
                que[t + 1].append((dir0[0], dir0[1]))
                flag = dir1[0]
            continue
        try:
            cur = temp_dir.index(flag)
            ret[temp_idx[cur]] = t
            for i in range(cur):
                que[t + 1].append((temp_dir[i], temp_idx[i]))
            for i in range(cur + 1, len(temp_dir)):
                que[t + 1].append((temp_dir[i], temp_idx[i]))
        except:
            ret[temp_idx[0]] = t
            for i in range(1, len(temp_idx)):
                que[t + 1].append((temp_dir[i], temp_idx[i]))
    ret = [i for i in ret if i != -1]
    return ret


if __name__ == '__main__':

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

    print('\n'.join(map(str, result)))
