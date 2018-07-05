#http://codeforces.com/contest/1003/problem/A

from collections import defaultdict

n=int(input())
a=[int(x) for x in input().split()]

freq=defaultdict(lambda:0,{})
for i in a:
	freq[i]+=1

frequencies=[]
for k in freq:
	frequencies.append(freq[k])

print(max(frequencies))

