#https://codeforces.com/contest/1234/problem/B2

import sys
import math
from collections import deque
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
n,k=takeInput()
friends=takeInput()
phone=deque()
msgs=0
display=set()
for f in friends:
    if(f not in display):
        if(msgs<k):
            display.add(f)
            msgs+=1
            phone.appendleft(f)
        elif(msgs==k):
            display.remove(phone.pop())
            phone.appendleft(f)
            display.add(f)
 
print(len(phone))
print(*phone)