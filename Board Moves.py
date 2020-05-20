#https://codeforces.com/contest/1353/problem/C

import sys
import math
from collections import Counter,defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
    
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    factor=8
    count=0
    for i in range(1,n//2+1):
        count+=(factor*i)
        factor+=8
 
    print(count)
 