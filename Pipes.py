#https://codeforces.com/contest/1234/problem/C

import sys
import math
from collections import defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
t=int(input())

while t!=0:
    t-=1
    n=int(input())
    row1=input()
    row2=input()
    row1=[int(x) for x in list(row1)]
    row2=[int(x) for x in list(row2)]
    #Simplifying 2 to 1 and the rest to 3 since they're equivalent
    for i,r in enumerate(row1):
        if(r==1 or r==2):
            row1[i]=1
        else:
            row1[i]=3
    for i,r in enumerate(row2):
        if(r==1 or r==2):
            row2[i]=1
        else:
            row2[i]=3
    
    row1=[0]+row1
    row2=[0]+row2
    rows=[[],row1,row2]
    r=1
    c=1
    #print(rows)
    possible=True
    #Proceed ahead and switch from 1 to 2 or 2 to 1 when you can!
    #If you can't switch then you're STUCK! 
    #Use possible to mark when STUCK
    for c in range(1,n+1):
        if(rows[r][c]==3):
            if(r==1):
                if(rows[2][c]==3):
                    r=2
                else:
                    possible=False
            elif(r==2):
                if(rows[1][c]==3):
                    r=1
                else:
                    possible=False

    if(r==1 or not possible):
        print("NO")
    else:
        print("YES")












