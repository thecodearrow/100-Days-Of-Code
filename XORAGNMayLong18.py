t=int(input())
while(t!=0):
    t=t-1
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[]
    
    for i in range(n):
        b.append(a[i]+a[i])
    
    xor=0    
    for i in range(n):
        xor^=b[i]
        
    print(xor)
    