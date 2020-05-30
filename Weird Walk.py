#https://www.codechef.com/LTIME84B/problems/WWALK/

import sys
import math
from collections import Counter,defaultdict
import heapq
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
    a=takeInput()
    b=takeInput()
    x1=0
    x2=0
    walk=0
    for i in range(n):
        if(x1==x2 and a[i]==b[i]):
            walk+=a[i]
        x1+=a[i]
        x2+=b[i]

    print(walk)

