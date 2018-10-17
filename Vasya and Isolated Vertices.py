#http://codeforces.com/contest/1065/problem/B

import math

n,m=[int(x) for x in input().split()]


x=(1+math.sqrt(1+8*m))/2  #(x*x-1)/2=m
not_isolated=math.ceil(x)
maximum=n-not_isolated
minimum=n-2*m #pairing 2 vertices for each m 
if(minimum<0):
	minimum=0

if(minimum>maximum):
	maximum=minimum
print(minimum,maximum)