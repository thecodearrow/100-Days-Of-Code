#https://codeforces.com/contest/1003/problem/C
#AC if you use PyPy3 

import heapq
n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
averages=[] #MAX HEAP
heapq.heapify(averages)
for i in range(0,n):
	sum=0
	for j in range(i,n):
		size=j-i+1
		sum+=a[j]
		if(size>=k):
			avg=sum/size
			heapq.heappush(averages,-avg)



print(-1*averages[0])