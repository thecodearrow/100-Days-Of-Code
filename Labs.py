#https://codeforces.com/contest/1236/problem/C

import math
import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 
 
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
 
n=int(input())
a=[[]for i in range(n)]
 
number=1
for i in range(n):
    if(i%2==0):
        for j in range(n):
            a[j].append(number)
            number+=1
    else:
        for j in range(n-1,-1,-1):
            a[j].append(number)
            number+=1
 
for i in range(n):
    print(*a[i])