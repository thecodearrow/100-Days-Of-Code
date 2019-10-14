#https://codeforces.com/contest/1244/problem/A

import math
t=int(input())
while t!=0:
    t-=1
    a,b,c,d,k=[int(x) for x in input().split()]
    pens=math.ceil(a/c)
    pencils=math.ceil(b/d)
    if(pens+pencils<=k):
        print(pens,pencils)
    else:
        print(-1)