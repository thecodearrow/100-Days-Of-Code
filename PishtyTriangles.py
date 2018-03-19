import itertools
def checkValidity(arr): 
     
    # check condition 
    a=arr[0]
    b=arr[1]
    c=arr[2]
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True    
        
n,q=[int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]
while(q!=0):
    q=q-1
    query=[int(x) for x in input().strip().split()]
    if(query[0]==1):
        #pos val 
        pos=query[1]
        val=query[2]
        arr[pos-1]=val
    elif(query[0]==2):
        start=query[1]-1
        end=query[2]
        current=arr[start:end]
        current=sorted(current)
        everything=list(itertools.combinations(current, 3))[::-1]
        count=0
        for e in everything:
            if(checkValidity(e)):
                print(sum(e))
                count=count+1
                break
        if(count==0):
            print(0)
                