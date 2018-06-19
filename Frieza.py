# Quick Code (Rated for Division 2)
frieza=["f","r","i","e","z","a"]

frieza=set(frieza)



n=int(input())

while(n!=0):
    n-=1 
    s=input()
    if(n!=0):
        junk=input()
    R=""
    good=0 
    bad=0
    for c in s:
        if(c in frieza):
            good+=1
            if(bad!=0):
                R+=str(bad)
                bad=0
            
        else:
            bad+=1
            if(good!=0):
                R+=str(good)
                good=0 
            
    last=s[-1] 
    if(last in frieza):
        R+=str(good)
    else:
        R+=str(bad)
    print(R)
        