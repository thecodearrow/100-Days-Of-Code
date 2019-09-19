#https://codeforces.com/contest/1221/problem/C

#https://codeforces.com/contest/1221/problem/B
 
import sys
import math
from collections import defaultdict
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
 
t=int(input())
while t!=0:
    t-=1
    c,m,ns=[int(x) for x in input().split()]
    only_c_m=min(c,m)
    ans=min(only_c_m,(c+m+ns)/3)
    print(int(ans))
 