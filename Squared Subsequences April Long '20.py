
#https://www.codechef.com/APRIL20B/problems/SQRDSUB

import sys
import math
from collections import defaultdict
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	input = sys.stdin.readline #Python Fast I/O
	

"""
Good Sequences = Either odd or divisble by 4 

Take the reverse approach

ANS= TOTAL - #Not good sequences

Total= N*(N+1) / 2

Not Good Seuquences= Sequences involving  single 2s in prime factorisation surrounded by odd numbers  EX: [odd,2,odd] [2,odd]
"""

def takeInput():
    return [int(x) for x in input().strip().split()]
 

t=int(input())

def is_single_two(number):
	#Has a single 2 in its prime factorisation 
	number=abs(number)
	if(number%2==0 and number%4!=0):
		return True
	return False
while t!=0:
	t-=1
	n=int(input())
	a=takeInput()
	good=0
	not_good=0
	total=(n*(n+1))/2
	single_twos=[]
	for i in range(n):
		if(is_single_two(a[i])):
			single_twos.append(i)

	for idx in single_twos:
		left_chain=0
		left_found=False
		#Go left
		for i in range(idx-1,-1,-1):
			if(a[i]%2==0):
				break
			left_found=True
			left_chain+=1
		#Go right
		right_found=False
		right_chain=0
		for i in range(idx+1,n):
			if(a[i]%2==0):
				break
			right_found=True
			right_chain+=1

		chain=1+left_chain+right_chain
		if(left_found and right_found):
			#Counting both sides like [odd,2,odd]
			chain+=(left_chain*right_chain)
		not_good+=chain
		
	good=int(total-not_good)
	print(good)



		







