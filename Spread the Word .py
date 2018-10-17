#https://www.codechef.com/SNCKQL19/problems/SPREAD2

#Spread the Word 

def min_days(A,n):
    ladder=A[0]
    stairs=A[0]
    days=1
    for i in range(1,n):
        if(i==n-1):
            return days 
        ladder+=A[i]
        stairs-=1
        if(stairs==0):
            days+=1
            stairs=ladder
        

t=int(raw_input())
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in raw_input().split()]
    ans=min_days(a,n)
    print(ans)