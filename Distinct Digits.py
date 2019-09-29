#https://codeforces.com/contest/1228/problem/A
 
 
import sys
import math
from collections import defaultdict,deque
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
def isDiffDigits(n):
    seen=set()
    while n!=0:
        d=n%10
        if(d in seen):
            return False
        else:
            seen.add(d)
        n=n//10
    return True
l,r=takeInput()
found=False
for x in range(l,r+1):
    if(isDiffDigits(x)):
        print(x)
        found=True
        break
 
if(not found):
    print(-1)