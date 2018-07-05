#http://codeforces.com/contest/1000/problem/A

from collections import defaultdict 

n=int(input())
prev=defaultdict(lambda:0,{})
now=[]
for i in range(n):
	ele=input()
	prev[ele]+=1 

for i in range(n):
	ele=input()
	if(prev[ele]>0):
		prev[ele]-=1 
	elif(prev[ele]==0):
		now.append(ele)


l=len(now)

print(l)

