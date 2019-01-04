#http://codeforces.com/contest/1091/problem/A

y,b,r=[int(x) for x in input().split()]

start=y 

while start>=1:
	if(start+1<=b and start+2<=r):
		break 
	start-=1 


print(start+start+1+start+2)