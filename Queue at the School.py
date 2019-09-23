
#https://codeforces.com/problemset/problem/266/B
import sys
import math
from collections import defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 

n,t=[int(x) for x in input().split()]
s=input().strip()
for i in range(t):
    s=s.replace("BG","GB")
print(s)