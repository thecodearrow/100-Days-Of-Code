#https://codeforces.com/contest/991 

a,b,c,n=[int(x) for x in input().split()]

fail=n-(a+b-c) #fail=n+c-a-b

if(fail<=0 or c>n  or c>a or c>b or fail>n): #more adge cases! 
	print(-1)
else:
	print(fail)