#https://codeforces.com/contest/1140/problem/B

"""
A string is good when either its first character is > or the last is <. 
Strings of type < … > are not good, as their first and last characters will never change and they 
will eventually come to the form < >.

"""

import sys
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
	ans=0
	min1=0 #minimum number of chars to be deleted before the first < 
	min2=0 #minimum number of chars to be deleted before the first > from the end 

	for c in s:
		if(c!="<"):
			break 
		min1+=1
		

	for c in s[::-1]:
		if(c!=">"):
			break
		min2+=1

	ans=min(min1,min2)
	print(ans)
		
		



		

		
				




		

