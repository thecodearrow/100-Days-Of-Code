#Archi and Comparsion Problem Code: NUMCOMP June Coofkoff 18

t=int(input())
 
 
 
 
while(t!=0):
    t-=1 
    a,b,n=[int(x) for x in input().split()]
    large=10**9 
    x=abs(a)
    y=abs(b)
    
    if((x==y and n%2==0) or a==b):
         print(0)
    elif(a>b):
        if(n%2!=0):
            print(1)
        else:
            if(x<y):
                print(2)
            else:
                print(1)
    elif(a<b):
        if(n%2!=0):
            print(2)
        else:
            if(x<y):
                print(2)
            else:
                print(1)
        
        