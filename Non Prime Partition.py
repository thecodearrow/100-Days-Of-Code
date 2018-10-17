#http://codeforces.com/contest/1038/problem/B

""""

The easiest way perhaps was to note that the sum of first is (n*n+1)/2 

Say k=n/2 or n+1/2 whichever is an integer... 

Then we can partition the numbers into two sets, one containing  k 
and the other containing the remaining integers, both of which will have 
k as a common factor.

"""
n=int(input())

if(n==1 or n==2):
	print("No")
else:
	print("Yes")
	k=n//2
	if(n%2!=0):
		k+=1
	set1=[k]
	set2=[]
	#remaining integers other than k
	for i in range(1,n+1):
		if(i!=k):
			set2.append(i)

	print(len(set1),*set1)
	print(len(set2),*set2) 


