#https://codeforces.com/contest/1353/problem/B



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
    n,k=takeInput()
    a=takeInput()
    b=takeInput()
    a=sorted(a)
    b=sorted(b,reverse=True)
    i=0
    j=0
    swaps=0
    while i<n and j<n and swaps<k:
        if(a[i]<b[j]):
            a[i],b[j]=b[j],a[i]
            swaps+=1
            i+=1
            j+=1
        else:
            break

    print(sum(a))
