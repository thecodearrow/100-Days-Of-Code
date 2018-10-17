#http://codeforces.com/contest/1064/problem/C

import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass
	
from collections import defaultdict
n=int(input())
s=input()

f=defaultdict(lambda:0)

for c in s:
	f[c]+=1

ans=""

for c in f:
	store=c*f[c]
	ans+=store

print(ans)