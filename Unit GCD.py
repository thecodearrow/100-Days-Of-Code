
#https://www.codechef.com/APRIL20B/problems/CARSELL

import sys
import math
from collections import defaultdict
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	input = sys.stdin.readline #Python Fast I/O
	

def takeInput():
    return [int(x) for x in input().strip().split()]
 
t=int(input())


#https://www.codechef.com/APRIL20B/

n=pow(10,6)+10
prime=[1 for i in range(n+100)]
s=int(math.sqrt(n))
for i in range(2,s+1):
	if(prime[i]):
		for j in range(2*i,n+1,i):
			prime[j]=0 #canceling out all multiples of i

while t!=0:
	t-=1
	n=int(input())
	days=0
	ans=[[]]
	added=[False for i in range(n+1)]
	for i in range(1,n+1):
		if(prime[i]):
			ans[0].append(i)
			added[i]=True
	
	for i in range(1,n+1):
		if(i<n and not added[i] and not added[i+1]):
			ans.append([i,i+1])
			added[i]=True
			added[i+1]=True
		elif(not added[i]):
			ans.append([i])
			added[i]=True

	print(len(ans))
	for row in ans:
		print(len(row),*row)



