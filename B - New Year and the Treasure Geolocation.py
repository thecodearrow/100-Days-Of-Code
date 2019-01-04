#http://codeforces.com/contest/1091/problem/B

import sys
import math
from collections import defaultdict

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass


n=int(input())
coords=[]
params=[]
for i in range(n):
	c=[int(x) for x in input().split()]
	coords.append(c)
for i in range(n):
	p=[int(x) for x in input().split()]
	params.append(p)


init=[coords[0][0],coords[0][1]]
answers=defaultdict(lambda:0)


for c in coords:
	c1,c2=c[0],c[1]
	for p in params:
		p1,p2=p[0],p[1]
		a=(c1+p1,c2+p2)
		answers[a]+=1


for a in answers:
	if(answers[a]==n):
		p=a
	
print(p[0],p[1])