#https://www.codechef.com/SNCK1A19/problems/CARDMGK

import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass

t=int(input())

while t!=0:
	t-=1
	count=0
	n=int(input())
	a=[int(x) for x in input().split()]
	end=n
	for i in range(1,n):
		if(a[i-1]>a[i]):
			count+=1
			end=i

	if(count<=1):
		#break it down into two sets of increasing numbers

		s1=a[:end]
		s2=a[end:]
		if(count==0):
			print("YES")
		else:
			x=min(s1)
			y=max(s2)
			
			if(x>=y):
				print("YES")
			else:
				print("NO")



	
	else:
		print("NO")