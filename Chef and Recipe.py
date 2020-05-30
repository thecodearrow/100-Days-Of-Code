#https://www.codechef.com/COOK118B/problems/CHEFRECP/

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
    a=[int(x) for x in input().split()]
    count=Counter(a)
    present={}
    chef=True

    i=0
    lookup={}
    while i<n:
        ele=a[i]
        if(ele in lookup):
            chef=False
            break
        lookup[ele]=True
        while i+1<n and a[i+1]==ele:
            i+=1
        i+=1

    for r in set(a):
        if(count[r] in present):
            chef=False
            break
        present[count[r]]=True

    if(chef):
        print("YES")
    else:
        print("NO")