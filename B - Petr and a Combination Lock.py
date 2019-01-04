#http://codeforces.com/contest/1097/problem/B

import sys
import math
from collections import defaultdict


def getInputFromLine():
	return [int(x) for x in input().split()]
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass

def isSumZero(queue,s,n):
	if(n<=0 and s%360==0):
		return True 
	elif(n<=0):
		return False
	
	item=queue[n-1]
	s+=item
	if(isSumZero(queue,s,n-1)):
		return True 
	s-=item
	s-=item 
	if(isSumZero(queue,s,n-1)):
		return True


	
		
n=int(input())
numbers=[]
for i in range(n):
	t=int(input())
	numbers.append(t)
	
if(isSumZero(numbers,0,n)):
	print("YES")
else:
	print("NO")