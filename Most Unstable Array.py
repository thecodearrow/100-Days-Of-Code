#https://codeforces.com/contest/1353/problem/A

import sys
import math
from collections import Counter,defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass
    


t=int(input())
while t!=0:
    t-=1
    m,n=[int(x) for x in input().strip().split()]
    if(m==1):
        print(0)
    elif(m==2):
        print(n)
    else:
        print(2*n)