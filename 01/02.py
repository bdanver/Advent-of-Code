#!/usr/bin/env python3
import sys  
with open('input.txt') as f:
   lines = list(map(int, f.readlines()))
count = 0 
total = 0
window_size = 3
window_sum = []

# get sums from sliding window 
for i in range(len(lines) - window_size + 1):
    total = sum(lines[i: i + window_size])
    window_sum.append(total)

# allows overlap when iterating through list
for pair in zip(window_sum, window_sum[1:]):
    if (pair[0] < pair[1]):
        count += 1

f.close()
print(count)
# not important, useful for future tho
#from collections import deque 
# seq = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# window = deque(maxlen=3)
# for char in seq:
#     window.append(char)
#     print(lines[i],''.join(list(window)))
#     print( ''.join(list(window)))