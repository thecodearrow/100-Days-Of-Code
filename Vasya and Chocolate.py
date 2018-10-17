#http://codeforces.com/contest/1065/problem/A

t=int(input())

while t!=0:
    t-=1
    money,a,b,c=[int(x) for x in input().split()]
    ans=0
    number=money//(a*c)
    ans+=(number*a+number*b)
    money-=(number*a*c)
    number=money//c 
    ans+=number
    print(ans)