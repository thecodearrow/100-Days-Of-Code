#https://codeforces.com/contest/1234/problem/A

import sys
import math
 
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
    ans=math.ceil(sum(a)/n)
    print(int(ans))