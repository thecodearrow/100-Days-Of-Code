#http://codeforces.com/contest/1009/problem/A

from collections import deque
n,m=[int(x) for x in input().split()]
games=[int(x) for x in input().split()]
cash=[int(x) for x in input().split()]
cash=deque(cash)

count=0
for g in games:
	if(cash):
		current=cash[0]
		if(current>=g):
			cash.popleft()
			count+=1 


print(count)