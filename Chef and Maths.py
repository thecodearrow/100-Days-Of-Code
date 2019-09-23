# https://www.codechef.com/problems/MATHL
t=int(input())
N=10**6
MOD=10**9+7
fact={}

fact[0]=1 

for i in range(1,N+1):
    fact[i]=(fact[i-1]*i)%MOD



cf={}
cf[0]=1
for i in range(1,N+1):
    cf[i]=fact[i]*cf[i-1]
    cf[i]=cf[i]%MOD
while t!=0:
    t-=1
    n=int(input())
    print(cf[n])