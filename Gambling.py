#http://codeforces.com/contest/1038/problem/C
from collections import deque 
n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

a=sorted(a)
b=sorted(b)

a=deque(a)
b=deque(b)

la=len(a)
lb=len(b)

score_a=0
score_b=0

for i in range(la+lb):
	if(i%2==0):
		#A plays 
		if(la>0):
			current=a[-1]
		else:
			current=0
		if(lb>0):
			compare=b[-1]
		else:
			compare=0
		
		if(compare>current and lb>0):
			ele=b.pop()
			lb-=1 
		elif(la>0):
			ele=a.pop()
			la-=1
			score_a+=ele
	else:
		if(lb>0):
			current=b[-1]
		else:
			current=0
		if(la>0):
			compare=a[-1]
		else:
			compare=0
		if(compare>current):
			ele=a.pop()
			la-=1 
		elif(lb>0):
			ele=b.pop()
			lb-=1
			score_b+=ele


print(score_a-score_b)

