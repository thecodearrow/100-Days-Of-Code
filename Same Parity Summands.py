#https://codeforces.com/contest/1352/problem/B

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
    if(n%2!=0):
        if(k%2==0):
            print("NO")
        else:
            ans=[]
            start=1
            for i in range(k-1):
                ans.append(start)
            rem=n-sum(ans)
            if(rem>0):
                ans.append(n-sum(ans))
                print("YES")
                print(*ans)
            else:
                print("NO")
    else:
        ans=[]
        start=2
        for i in range(k-1):
            ans.append(start)
        rem=n-sum(ans)
        if(rem>0):
            ans.append(n-sum(ans))
            print("YES")
            print(*ans)
        else:
            start=1
            ans=[]
            for i in range(k-1):
                ans.append(start)
            rem=n-sum(ans)
            if(rem>0 and rem%2!=0):
                ans.append(n-sum(ans))
                print("YES")
                print(*ans)
            else:
                print("NO")
 
 
 