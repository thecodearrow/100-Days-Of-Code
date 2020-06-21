#https://www.codechef.com/COOK119B/problems/MAXMEX/


import sys
import math
from collections import Counter,defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass
    


t=int(input())
while t!=0:
    t-=1
    n,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    mux=1
    present=Counter(a)
    possible=True
    for ele in range(1,m):
        if(ele not in present):
            possible=False
            break
    if(possible):
        count=0
        for ele in a:
            if(ele!=m):
                count+=1
        
        print(count)
    else:
        print(-1)

    


