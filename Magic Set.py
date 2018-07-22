#July Long 2018 Prob 1
#https://www.codechef.com/JULY18B/problems/MGCSET
import math

def nCr(n,r):
    fact = math.factorial
    return fact(n) / fact(r) / fact(n-r)

t=int(input())
for test in range(t):
	n,m=[int(x) for x in input().split()]
	a=[int(x) for x in input().split()]
	c=0 #count_divisible_by_m
	for ele in a:
		if(ele%m==0):
			c+=1

	ans=0 #number of subsequences that can be made with all those numbers in a sequence i.e nc1+nc2+....
	
	for i in range(1,c+1):
		ans+=nCr(c,i)

	print(int(ans))