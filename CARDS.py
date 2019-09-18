#By thecodearrow, contest: Codeforces Round #586 (Div. 1 + Div. 2), problem: (A)
 
 
#https://codeforces.com/contest/1220/problem/A
 
import sys
import math
from collections import defaultdict
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
n=int(input())
s=input()
freq={0:0,1:0}
for c in s:
    if(c=='z'):
        freq[0]+=1
    elif(c=='n'):
        freq[1]+=1
 
ans=[]
while freq[1]!=0:
    ans.append(1)
    freq[1]-=1
 
while freq[0]!=0:
    ans.append(0)
    freq[0]-=1
 
print(*ans)