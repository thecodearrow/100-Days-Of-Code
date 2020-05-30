#https://www.codechef.com/LTIME84B/problems/LOSTWKND


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
    a1,a2,a3,a4,a5,p=takeInput()
    hours=(a1+a2+a3+a4+a5)*p
    if(hours<=24*5):
        print("No")
    else:
        print("Yes")
