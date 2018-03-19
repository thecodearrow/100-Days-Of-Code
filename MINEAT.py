# PARTIALLY SOLVED
import sys

array=[]

def checkCorrectK(bananas,k,h):
    count=0
    for b in bananas:
        slash=b/k 
        if(slash==0):
            count=count+1
        elif(slash.is_integer()):
            count=count+int(slash)
        else:
            count=count+int(slash)+1
    if(count==h):
        return True
    else:
        return False
        
def binTraversal(lower,upper,bananas,h):
    if(lower==upper):
        return 1
    else:
        
        mid=(lower+upper)//2
        mids=[]
        if(checkCorrectK(bananas,mid,h)):
           
            binTraversal(lower,mid,bananas,h)
            binTraversal(mid+1,upper,bananas,h)
            array.append(mid)
            
    
            
            

    
    
 
t=int(input())
while(t!=0):
    t=t-1
    temp=[int(x) for x in input().strip().split()]
    n=temp[0]
    h=temp[1]
    bananas=[int(x) for x in input().strip().split()]
    sorted(bananas)
    lower=sum(bananas)//k
    upper=max(bananas)
    if(h==len(bananas)):
        print(max(bananas))
    else:
        array=[]
        binTraversal(lower,upper,bananas,h)
        print(min(array))
        

  
