#May CookOff 2018 Secret Recipe

t=int(input())
 
while(t!=0):
    t=t-1
    x1,x2,x3,v1,v2=[int(x) for x in input().strip().split()]
    
    t1=abs(x3-x1)/v1
    t2=abs(x3-x2)/v2
    if(t1<t2):
        print("Chef")
    elif(t2<t1):
        print("Kefa")
    else:
        print("Draw") 