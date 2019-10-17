#https://codeforces.com/contest/1236/problem/B

import math
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 
 
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 

n,m=takeInput()
modulo=10**9+7
part1=pow(2,m,modulo)-1
ans=pow(part1,n,modulo)
print(ans)
