#https://www.codechef.com/SEPT19B/problems/CHEFK1/

t=int(input())
import math

while t!=0:
    t-=1
    n,m=[int(x) for x in input().split()]
    max_edges=((n*(n+1))/2) #including self loops
    if(m<n-1 or m>max_edges):
        print(-1)
    elif(n==1 and m==0):
        print(0)
    elif(n==1 and m==1):
        print(1)
    elif(n==2 and m==1):
        print(1)
    elif(m>=n-1 and m<=n+1):
        print(2)
    elif(m<=2*n):
        print(3)
    else:
        print(min(n,math.ceil((2*m-n)/n)))
