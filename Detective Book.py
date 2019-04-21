import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass

from collections import defaultdict
n=int(input())
a=[int(x) for x in input().split()]

days=0
page={}
p=1
for ele in a:
	page[p]=ele
	p+=1

visited=defaultdict(lambda:False)
end=1
for p in range(1,n+1):
	if(not visited[p]):
		days+=1
	if(page[p]>=end):
		end=page[p]
		for i in range(p,page[p]+1):
			visited[i]=True