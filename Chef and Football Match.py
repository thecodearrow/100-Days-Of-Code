#https://www.codechef.com/problems/WATCHFB/


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


t=int(input())
while t!=0:
    t-=1
    q=int(input())
    score_A=0
    score_B=0
    while q!=0:
        q-=1
        idx,one,two=takeInput()
        found=False
        if(idx==1):
            score_A=one
            score_B=two
            found=True
        else:
            if(one==two):
                score_A=one
                score_B=two
                found=True
            else:
                check1=one>=score_A and two>=score_B
                check2=two>=score_A and one>=score_B
                if(check1 and check2):
                    found=False
                else:
                    found=True
                    if(check1):
                        score_A=one
                        score_B=two 
                    else:
                        score_A=two
                        score_B=one



        if(found):
            print("YES")
        else:
            print("NO")



