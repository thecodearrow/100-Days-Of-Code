#http://codeforces.com/contest/1214/problem/B

b=int(input())
g=int(input())
n=int(input())
ans=n+1
for i in range(b+1,n+1):
    ans-=1
for i in range(g+1,n+1):
    ans-=1
print(ans)