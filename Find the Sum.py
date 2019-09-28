#https://www.codechef.com/LTIME76B/problems/PAIRSUM2


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
    n,q=takeInput()
    b=takeInput()
    b=[0]+b
    odds=[0]*(n)
    evens=[0]*(n)
    for i in range(1,n):
        ele=b[i]
        if(i%2==0):
            evens[i]=evens[i-1]+ele
            odds[i]=odds[i-1]
        else:
            odds[i]=odds[i-1]+ele
            evens[i]=evens[i-1]


    for query in range(q):
        l,r=takeInput()
        if((l+r)%2==0):
            print("UNKNOWN")
        else:
            end=max(l,r)
            start=min(l,r)
            
            if(start%2==0):
                ans=evens[end-1]-odds[end-1]
                if(start!=1):
                    ans=(evens[end-1]-evens[start-1])-(odds[end-1]-odds[start-1])
            else:
                ans=odds[end-1]-evens[end-1]
                if(start!=1):
                    ans=(odds[end-1]-odds[start-1])-(evens[end-1]-evens[start-1])
            print(ans)

            

