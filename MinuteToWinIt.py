#https://www.hackerrank.com/contests/w38/challenges/minute-to-win-it
from collections import defaultdict
n,k=[int(x) for x in input().split()]
points=[int(x) for x in input().split()]
#draw a line with slope k and then compute difference between the line and the points given

line=[]

for i in range(n):
    line.append(k*i) #0,k,2k......

diff=defaultdict(lambda:0)
for i in range(n):
    d=line[i]-points[i]
    diff[d]+=1

count=0
for d in diff:
    if(diff[d]>count):
        count=diff[d]

print(n-count)