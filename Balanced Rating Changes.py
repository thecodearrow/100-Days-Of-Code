#https://codeforces.com/contest/1237/problem/A

import math
import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 
 
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
can_be_changed={}
n=int(input())
a=[]
 
for i in range(n):
    number=int(input())
    a.append(number)
 
for i in range(n):
    ele=a[i]
    if(ele%2!=0):
        can_be_changed[i]=ele
    a[i]=math.ceil(a[i]/2)
 
current_sum=sum(a)
for i in range(n):
    if(current_sum==0):
        break
    if(i in can_be_changed):
        a[i]=math.floor(can_be_changed[i]/2)
        current_sum-=1
 
for ele in a:
    print(ele)
 
 