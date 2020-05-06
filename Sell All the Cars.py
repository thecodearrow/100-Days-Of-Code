
#https://www.codechef.com/APRIL20B/problems/CARSELL

import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	input = sys.stdin.readline #Python Fast I/O
	

def takeInput():
    return [int(x) for x in input().strip().split()]
 
t=int(input())
while t!=0:
	t-=1
	n=int(input())
	cars=takeInput()
	cars=sorted(cars)[::-1]
	for i in range(n):
		if(cars[i]-i>=0):
			cars[i]-=i
		else:
			cars[i]=0
	modulo=10**9+7
	print(sum(cars)%modulo)