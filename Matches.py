import sys
import math
from itertools import combinations
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 

t=1
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    q=int(input())
    bill=0
    while q!=0:
        l,r,min_cost=[int(x) for x in input().split()]
        items=a[l:r+1]
        items=sorted(items)
        bill+=bisect.bisect_left(items,min_cost)  
        

    print(bill)