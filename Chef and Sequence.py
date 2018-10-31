#https://www.codechef.com/SNCK1B19/problems/CHFAR


t=int(input())

def sqsum(a):
    ans=0
    for ele in a:
        ans+=(ele**2)

    return ans
while t!=0:
    t-=1
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    a=sorted(a)[::-1]
    for i in range(k):
        a[i]=1


    if(sqsum(a)<=sum(a)):
        print("YES")
    else:
        print("NO")



