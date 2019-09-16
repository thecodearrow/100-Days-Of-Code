
#https://www.codechef.com/FLMOCK01/problems/ALTARAY

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
    a=[int(x) for x in input().split()]
    ans=[1 for x in a]
    signs=[]
    for ele in a:
    	if(ele>0):
    		signs.append(1)
    	else:
    		signs.append(-1)
    for i in range(n-2,-1,-1):
    	ele=signs[i]
    	prev=signs[i+1]
    	if(ele+prev==0):
    		#opposite signs
    		ans[i]=ans[i+1]+1

    print(*ans)


    