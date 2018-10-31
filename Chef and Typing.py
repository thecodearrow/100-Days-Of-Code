#https://www.codechef.com/SNCK1A19/problems/TYPING

import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass



	
t=int(input())
L={'d','f'}
R={'j','k'}
while t!=0:
	t-=1
	words={}
	sum1=0
	n=int(input())
	for i in range(n):
		s=input()
		current=2
		for i in range(1,len(s)):

			prev=s[i-1]
			curr=s[i]
			if((prev in L and curr in L) or (prev in R and curr in R)):
				current+=4
			else:
				current+=2
		if(s in words):
			current=words[s]/2
		else:
			words[s]=current
		
		sum1+=current
		

	ans=int(sum1)
	print(ans)

	