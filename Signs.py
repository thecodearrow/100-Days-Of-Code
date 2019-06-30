#https://www.codechef.com/JUNE19B/problems/RSIGNS

def count_unique_digits_front_and_back(i,k):
    s=set() 
    count=0
    n=i
    if(n==0):
        count=1
    while n!=0:
        d=n%10
        if(d not in s):
            count+=1
            s.add(d)
        n=n//10
    n=10**k-i-1
    if(n==0 and n not in s):
        count+=1
    while n!=0:
        d=n%10
        if(d not in s):
            count+=1
            s.add(d)
        n=n//10
    return count

t=int(input())
modulo=10**9+7

#observe the pattern 10,20,40,80,160.... GP series a=10,r=2
while t!=0:
    t-=1
    k=int(input())
    r=2
    a=10
    ans=a*(pow(r,k-1,modulo)) 
    print(int(ans%modulo))





