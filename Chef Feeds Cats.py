#https://www.codechef.com/LTIME76B/problems/CATFEED/

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


t=int(input())
while t!=0:
    t-=1
    n,m=takeInput()
    feed=defaultdict(lambda:0)
    a=takeInput()
    fair=True
    for c in a:
        if(feed[c]==0):
            feed[c]+=1
        else:
            for i in range(1,n+1):
                if(feed[i]<feed[c]):
                    fair=False
                    break
            if(fair):
                feed[c]+=1
            else:
                break

    if(fair):
        print("YES")
    else:
        print("NO")        

