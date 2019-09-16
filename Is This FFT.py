#https://www.codechef.com/FLPAST01/problems/POLMUL/
from collections import defaultdict
t=int(input())
while t!=0:
    t-=1
    n,m=[int(x) for x in input().split()]
    P=[int(x) for x in input().split()]
    Q=[int(x) for x in input().split()]
    coefficient_at=defaultdict(lambda:0)
    for i,p in enumerate(P):
        for j,q in enumerate(Q):
            coefficient_at[i+j]+=p*q
    ans=[]
    for i in range(n+m-1):
        ans.append(coefficient_at[i])
    print(*ans)
