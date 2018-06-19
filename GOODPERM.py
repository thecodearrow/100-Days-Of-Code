#Good Permutations Problem Code: GOODPERM June Cookoff 2018

import itertools
t=int(input())
while(t!=0):
    t-=1 
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    numbers=[] #1 through n 
    for i in range(1,n+1):
        numbers.append(i)
    missing_indices=[]
    index=0
    for ele in a:
        if(ele!=0):
            numbers.remove(ele) 
        else:
            missing_indices.append(index)
        index+=1 
    
    r=len(numbers)
    permu=list(itertools.permutations(numbers,r)) 
    times=len(permu)


    
    index=0
    goods=[]
    for i in range(times):
        complete_permu=list(a)
        p=permu[i]
        inside_index=0
        for m in missing_indices:
            complete_permu[m]=p[inside_index]
            inside_index+=1
        goods.append(complete_permu)
   
    g=goods[0]
    lg=len(g)
    answer=0
    for g in goods:
        good=0 
        for i in range(lg-1):
            if(g[i+1]>g[i]):
                good+=1 
        if(good==k):
            answer+=1 
    print(answer)
            
    
            
            
        
    