"""
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

"""

#!/bin/python3

import sys


n = int(input().strip())
b=bin(n)[2:]
count=0
maxCount=0
for char in b:
    if(char=='0'):
        count=0
    else:
        count=count+1
    if(maxCount<count):
        maxCount=count
print(maxCount)        