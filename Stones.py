 #https://codeforces.com/contest/1236/problem/A

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
 
 
 
t=int(input())
while t!=0:
    t-=1
    a,b,c=takeInput()
    stones1=0
    stones2=0

    while b!=0 and c>=2:
        c-=2
        b-=1
        stones1+=3
    while a!=0 and b>=2:
        b-=2
        a-=1
        stones1+=3

    while a!=0 and b>=2:
        b-=2
        a-=1
        stones2+=3
    while b!=0 and c>=2:
        c-=2
        b-=1
        stones2+=3


    print(max(stones1,stones2))