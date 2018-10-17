#http://codeforces.com/contest/1038/problem/0
from collections import defaultdict 
n,k=[int(x) for x in input().split()]
s=input()
freq=defaultdict(lambda:0)

for c in s:
	freq[c]+=1

minimum=10**9
for i in range(65,65+k):
	minimum=min(minimum,freq[chr(i)])

print(minimum*k)


