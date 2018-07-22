#http://codeforces.com/contest/1006/problem/B

n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]

sorted_a=sorted(a)[::-1]
profits=[]
for i in range(k):
	profits.append(sorted_a[i])

sum1=sum(profits)
counts=[]


if(k==1):
	print(sorted_a[0])
	print(n)
else:
	c=0
	index=1
	for i in range(n):
		if(len(profits)==0):
				break
		c+=1
		if(a[i] in profits):
			if(len(profits)==1):
				#last element
				c+=n-i-1
			profits.remove(a[i])
			index+=1
			counts.append(c)
			c=0
			

	print(sum1)
	for i in counts:
		print(i,end=' ')