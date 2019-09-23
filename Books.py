# https://www.codechef.com/BIT22019/problems/BIT2A/

t=int(input())
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    ans=[0 for i in range(n)]
    count=0
    for i in range(n-2,-1,-1):
        count+=1
        if(a[i]<a[i+1]):
            ans[i]=count
        else:
            ans[i]=ans[i+1]
    print(*ans)
