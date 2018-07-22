#https://www.codechef.com/JULY18B/problems/NMNMX

from functools import reduce 
import operator as op

#efficient factorial = PRECOMPUTE FACTORIALS ;) 
#Ref https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
#AC in PyPy

fact={}

fact[0]=1 

for i in range(1,5001):
	fact[i]=fact[i-1]*i

def ncr(n, r):
	if(r>n):
		return 0
	return fact[n] // fact[n-r] // fact[r]

def expoGivenI(n,k,i,precomputed):
	#returns the number of combinations in which element is not the global minimum
	#total no of combos in which a particular element is always present - noOfWaysInWhichThatElementIsMin- noOfWaysInWhichThatElementIsMax
	e= precomputed- ncr(n-i-1,k-1)-ncr(i,k-1)
	return e

    
t=int(raw_input())

while(t!=0):
	t-=1
	n,k=[int(x) for x in raw_input().split()]
	a=[int(x) for x in raw_input().split()]
	a=sorted(a)
	middle_eles=[]
	for i in range(1,n-1):
		middle_eles.append(a[i])

	exponents=[ncr(n-2,k-2)]  #n-2Ck-2 is the expo of the second number
	mid=n//2
	precomputed=ncr(n-1,k-1) #total no of combos in which a particular element is always present 
	for index in range(2,mid):
		exponents.append(expoGivenI(n,k,index,precomputed))

	mirror=exponents[::-1]

	if(n%2!=0):
		#n happens to be odd 
		#calculate middle element
		exponents.append(expoGivenI(n,k,mid,precomputed))

	exponents+=mirror

	products=[]
	for i in range(n-2):
		p=pow(middle_eles[i],exponents[i],10**9+7) #mid[i] ^ expo
		products.append(p)

	ans=reduce(op.mul,products,1)


	print(pow(ans,1,10**9+7))