#http://codeforces.com/contest/1006/problem/A

t=int(input())
a=[int(x) for x in input().split()]

sorted_a=set()
for ele in a:
	sorted_a.add(ele-1)
	sorted_a.add(ele)
	sorted_a.add(ele+1)

sorted_a=sorted(sorted_a)

for ele in sorted_a:
	if(ele%2==0):
		a=[ele-1 if x==ele else x for x in a]
	else:
		a=[ele+1 if x==ele else x for x in a]

for i in a:
	print(i,end=' ')