n=int(input())

a=[int(z) for z in input().split()]


count=0 
maximum=-10**7
current=a[0]
for ele in a:
    if(ele<current):
        count=1 
    else:
        count+=1 
    current=ele
    maximum=max(count,maximum)
    
print(maximum)