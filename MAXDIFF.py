
#https://www.codechef.com/FLMOCK01/problems/MAXDIFF

import sys
import math

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


t=int(input())
while t!=0:
    t-=1
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    a=sorted(a)[::-1]
    k=max(k,n-k)
    print(sum(a[:k])-sum(a[k:]))


    