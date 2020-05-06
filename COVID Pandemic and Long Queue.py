#https://www.codechef.com/APRIL20B/problems/COVIDLQ


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
	spots=[int(x) for x in input().split()]
	allowed=True
	distance=6
	for ele in spots:
		if(ele==0):
			distance+=1
		else:
			if(distance<6):
				allowed=False
			distance=1




	if(allowed):
		print("YES")
	else:
		print("NO")