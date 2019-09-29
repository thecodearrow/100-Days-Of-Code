#https://codeforces.com/contest/1228/problem/B

import sys
import math
from collections import defaultdict,deque
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
r,c=takeInput()
rows=takeInput()
cols=takeInput()
filled=[[False for i in range(c+2)]for j in range(r+2)]
idx=1
for i in rows:
    for j in range(1,i+2):
        filled[idx][j]=True
    idx+=1
 
idx=1
for i in cols:
    for j in range(1,i+2):
        filled[j][idx]=True
    idx+=1
 
possible=True
free=0
for i in range(1,r+1):
    for j in range(1,c+1):
        if(not filled[i][j]):
            free+=1
 
#Verify
 
filled=[[False for i in range(c+1)]for j in range(r+1)]
idx=1
for i in rows:
    for j in range(1,i+1):
        key=str(idx)+":"+str(j)
        filled[idx][j]=True
    idx+=1
 
idx=1
for i in cols:
    for j in range(1,i+1):
        filled[j][idx]=True
    idx+=1
idx=1
for i in rows:
    j=1
    current_count=0
    while j<=c and filled[idx][j]:
        current_count+=1
        j+=1
    #print(current_count,i)
    if(current_count!=i):
        possible=False
        break
    idx+=1
idx=1
for i in cols:
    j=1
    current_count=0
    while j<=r and filled[j][idx]:
        current_count+=1
        j+=1
    #print(current_count,i)
    if(current_count!=i):
        possible=False
        break
    idx+=1
if(not possible):
    print(0)
else:
    print(pow(2,free,10**9+7))