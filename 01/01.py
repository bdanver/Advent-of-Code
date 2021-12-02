#!/usr/bin/env python3
import sys
with open('input.txt') as f:
   lines = list(map(int, f.readlines()))
count = 0
for pair in zip(lines, lines[1:]):
    #print('0: ', pair[0], '1: ', pair[1])
    if (pair[0] < pair[1]):
        count += 1

f.close()
print(count)