#https://www.codechef.com/problems/FFL

import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    input = sys.stdin.readline 
    

def takeInput():
    return [int(x) for x in input().strip().split()]
 
        
t=int(input())
while t!=0:
	t-=1
	n,s=takeInput()
	prices=takeInput()
	forward=takeInput()
	min_f=float("inf")
	min_d=float("inf")
	for i in range(n):
		if(forward[i]):
			min_f=min(min_f,prices[i])
		else:
			min_d=min(min_d,prices[i])

	cost=s+min_f+min_d
	if(cost>100):
		print('no')
	else:
		print('yes')
