

#https://codeforces.com/contest/1220/problem/B

#TLE :/

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass

def isValid(gcd,store,n):
    a=[gcd]
    for i in range(1,n):
        a.append((store[0][i]//gcd))
    for i in range(n):
        for j in range(n):
            if(i!=j):
                if((a[i]*a[j])!=store[i][j]):
                    return False

    return True



n=int(input())
ans=[]
store=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    store.append(arr)

gcd=math.gcd(store[0][0],store[0][1])
for i in range(2,n):
    gcd=math.gcd(gcd,store[0][i])

i=1
first_value=1
#Go through all factors of gcd 
for i in range(1,int(math.sqrt(gcd))+1):
    if(isValid(gcd/i,store,n)):
        first_value=gcd/i
        break
    elif(isValid(i,store,n)):
        first_value=i
        break
    i+=1

answer=[int(first_value)]
for i in range(1,n):
    answer.append(int(store[0][i]/answer[0]))

print(*answer)