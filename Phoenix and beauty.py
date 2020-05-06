#https://codeforces.com/contest/1348/problem/B

import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
    
 
import math
def takeInput():
    return [int(x) for x in input().strip().split()]
 
        
 
t=int(input())
def beauty_check(a,n,k):
    sums=set()
    for i in range(n-k+1):
        current_sum=0
        for j in range(k):
            current_sum+=a[i+j]
        sums.add(current_sum)
    if(len(sums)==1):
        return True
    return False
while t!=0:
    t-=1
    n,k=takeInput()
    a=takeInput()
    chars=set()
    for i in range(n):
        chars.add(a[i])
    if(len(chars)>k):
        print(-1)
    elif(beauty_check(a,n,k)):
        #already beautiful!
        print(len(a))
        print(*a)
    else:
        num_chars=len(chars)
        for i in range(1,n+1):
            if(len(chars)==k):
                break
            if(i not in chars):
                chars.add(i)
 
        beautiful=[]
        pattern=sorted(list(chars))
        for i in range(n):
            for j in range(k):
                beautiful.append(pattern[j])
 
        print(len(beautiful))
        print(*beautiful)
 
 
            
 
 
        