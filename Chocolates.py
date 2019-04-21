#https://codeforces.com/contest/1139/problem/B
n=int(input())
a=[int(x) for x in input().split()]
a=a[::-1]
curr=a[0]
score=curr
for i in range(1,n):
    curr=min(curr-1,a[i])
    if(curr<=0):
        break 
    score+=curr
print(score)
