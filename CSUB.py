
#https://www.codechef.com/FLMOCK01/problems/CSUB

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
    n=int(input())
    s=input()
    count=0
    #The zeroes in between don't really matter 
    for b in s:
    	if(b=="1"):
    		count+=1
    ans=int(count*(count+1)/2)
    print(ans)

