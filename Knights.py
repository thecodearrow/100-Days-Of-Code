#https://codeforces.com/contest/1221/problem/B


 
import sys
import math
from collections import defaultdict
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
 
n=int(input())
for i in range(n):
    if(i%2==0):
        for j in range(n):
            if(j%2==0):
                print('W',end='')
            else:
                print('B',end='')
    else:
        for j in range(n):
            if(j%2==0):
                print('B',end='')
            else:
                print('W',end='')
    print()
 
 
