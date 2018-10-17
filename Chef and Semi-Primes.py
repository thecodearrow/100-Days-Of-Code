from collections import defaultdict
import math

#precomputation rocks! :D
def semi_prime_sums():
	N=200
	prime=defaultdict(lambda:True)
	prime[1]=False 

	limit=int(math.sqrt(N)+1)

	for i in range(2,limit):
		if(prime[i]):
			for j in range(2*i,N+1,i):
				prime[j]=False 
	primes=[]			
	for i in range(2,200):
		if(prime[i]):
			primes.append(i)

	

	semiprimes=[]

	for i in range(len(primes)):
		for j in range(i+1,len(primes)):
			s=primes[i]*primes[j]
			if(s<=200):
				semiprimes.append(s)


	check={}


	for a in semiprimes:
		for b in semiprimes:
			n=a+b
			if(n<=200):
				check[n]=True

	return check


t=int(input())
check=semi_prime_sums()
while t!=0:
	t-=1
	n=int(input())
	if(n in check):
		print("YES")
	else:
		print("NO")




