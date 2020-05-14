#https://codeforces.com/contest/1352/problem/A

 
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
    n=int(input())
    rounds=[]
    pow10=1
    while n:
        d=n%10
        if(d!=0):
            rounds.append(pow10*d)
        pow10*=10
        n//=10
    print(len(rounds))
    print(*rounds)
 