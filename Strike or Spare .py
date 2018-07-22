t=int(input())

import math

for testcase in range(t):
	n=int(input())
	""""


	total=9*10**(n-1) #9*10*10.... 
	half_count=math.ceil(n/2) 
	palindromes=9*10**(half_count-1) 
	gcd=math.gcd(total,palindromes)
	p=palindromes//gcd 
	q=total//gcd 
	print(p,q)
	
	""" 

	p=1
	q=10**((n)//2)
	print(p,q)