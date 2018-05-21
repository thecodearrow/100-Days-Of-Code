
    
t=int(input())

def gcd(a, b): 
    if a == 0 :
        return b 
     
    return gcd(b%a, a)


while(t!=0):
    t=t-1
    n=int(input())
    arr=[int(x) for x in input().strip().split(' ')]
    checker=arr[0]
    eureka=False
    for i in arr:
        if(gcd(checker,i)==1):
            eureka=True
            break
    
    if(eureka):
        print(0)
    else:
        print(-1)