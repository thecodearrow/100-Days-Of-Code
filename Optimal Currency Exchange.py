#http://codeforces.com/contest/1214/problem/A

n=int(input())
d=int(input())
e=int(input())
e=5*e
ans=float("inf")
for i in range(0,n+1):
    rem1=i-((i//d)*d)
    j=n-i+rem1
    rem2=j-((j//e)*e)
    ans=min(rem2,ans)
print(ans)