#https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fd0d

import math
import sys
from collections import defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 
def takeInput():
    return [int(x) for x in input().strip().split()]
  
 
t=int(input())
for test_case in range(1,t+1):
    n,m,q=takeInput()
    torn_pages=takeInput()
    torn=[False for i in range(n+1)]
    for page in torn_pages:
        torn[page]=True
    readers=takeInput()
    can_be_read=[0 for i in range(n+1)]
    ans=0
    memo={}
    for r in readers:
        if(r not in memo):
            read_count=0
            for i in range(r,n+1,r):
                if(not torn[i]):
                    read_count+=1
            memo[r]=read_count
        ans+=memo[r]
    
    print("Case #"+str(test_case)+": "+str(ans))
        