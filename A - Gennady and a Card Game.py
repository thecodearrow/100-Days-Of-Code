#http://codeforces.com/contest/1097/problem/A

import sys
import math
from collections import defaultdict


def getInputFromLine():
	return [int(x) for x in input().split()]
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass



temp=input()
num,kind=temp[0],temp[1]
temp=[x for x in input().split()]
suit=set()
numbers=set()
for c in temp:
	numbers.add(c[0])
	suit.add(c[1])

if(num in numbers or kind in suit):
	print("YES")
else:
	print("NO")