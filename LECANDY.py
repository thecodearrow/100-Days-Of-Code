
#https://www.codechef.com/FLMOCK02/problems/LECANDY

import sys
import math

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass


t=int(input())
while t!=0:
    t-=1
    n,c=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    required=sum(a)
    if(required<=c):
        print("Yes")
    else:
        print("No")
