#https://www.codechef.com/NOV18B/problems/CHFTIRED

#Since it is given that a and b are positive integers< you can ALWAYS make A=B

t=int(input())

while t!=0:
	t-=1
	a,b=[int(x) for x in input().split()]
	print("YES")