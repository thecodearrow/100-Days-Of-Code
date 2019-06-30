#https://www.codechef.com/JUNE19B/problems/SUMAGCD


"""
Just picking the largest vs rest  => ans1
Or
Second largest vs the rest => ans2 


ans=max(ans1,ans2)


"""

def GCD(x, y): 
   while(y): 
       x, y = y, x % y 

   return x 

t=int(input())
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    a=list(set(a))
    a=sorted(a)
    n=len(a)
    last=a[-1]
    gcd1=last
    gcd2=a[0]
    if(n>1 and n-1!=1):
        gcd2=GCD(a[0],a[1])
    for i in range(n-1):
        ele=a[i]
        gcd2=GCD(gcd2,ele)
    ans1=gcd1+gcd2
    ans2=1
    if(n>=2):
        gcd1=a[-2]
        gcd2=a[0]
        if(n-2!=1):
            gcd2=GCD(a[0],a[1])
        for i in range(n):
            if(i!=n-2):
                ele=a[i]
                gcd2=GCD(gcd2,ele)
        ans2=gcd1+gcd2
  
   
        
    print(max(ans1,ans2))