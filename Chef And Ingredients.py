#https://www.codechef.com/JUNE19B/problems/CHFING
#The numbers become continuous once we have k consecutive numbers
#So it's all about pattern finding here

#ans= (k-1)+ .... keep reducing by a factor of n-1
import math
t=int(input())
modulo=10**9+7
while t!=0:
    t-=1
    n,k=[int(x) for x in input().split()]
    x=(k-1)//(n-1)
    a=k-1
    d=1-n
    tx=a+(x*d)
    if(tx<0):
        x=(k-n)//(n-1)
        tx=a+((x)*d)

    #we have the first term and last term, so we can can calculate N
    no_of_terms=(tx-a+1-n)//(1-n)
    #calculate Sum of terms in AP and that's the answer
    #sx=n/2 * (a+l)
    ans=(no_of_terms*(a+tx))//2
    print(ans%modulo)