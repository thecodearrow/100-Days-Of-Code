#https://codeforces.com/contest/1217/problem/A

import math
t=int(input())
while t!=0:
    t-=1
    s,i,e=[int(x) for x in input().split()]
    d=s-i
    if(e==0):
        if(s>i):
            print(1)
        else:
            print(0)
    else:
        if(e%2==0):
            total=(e+1)//2+math.ceil(d/2)
        else:
             total=(e+1)//2+math.floor(d/2)
        print(min(max(total,0),e+1))