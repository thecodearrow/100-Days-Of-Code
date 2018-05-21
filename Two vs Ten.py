#LUNCHTIE TWOVSTEN APRIL 2018
t=int(input())
for i in range(t):
    x=int(input())
    last=x%10
    if(x==1):
        print(-1)
        
    elif(x%10==0):
        print(0)
    
    
    elif(last==5):
        print(1)
    
    else:
        print(-1)