#HAVE NOT FULLY SOLVED IT!!! NEEDS TO BE FIXED....

import numpy as np
import bisect
t=int(input())
while(t!=0):
    t=t-1
    n,q=[int(x) for x in input().split()]
    snakes_dict={}
    snakes=sorted([int(x) for x in input().split()])
    snakesnp=np.array(snakes)
    index=0
    suffix_sum=[0]*n
    for s in snakes:
        snakes_dict[s]=index 
        index=index+1
    index=n-2
    suffix_sum[n-1]=snakes[n-1]
    while(index>=0):
        suffix_sum[index]=snakes[index]+suffix_sum[index+1]
        index=index-1
    while(q!=0):
        q=q-1
        k=int(input())
        find=bisect.bisect_left(snakes,k-0.5)-1 #making sure we get the insertion point as unique since duplicates are possible
    
        
        ans=n-find-1 #remaining snakes >=k 
        low=0
        high=find
     
        while(low<=high):
            mid=(low+high)//2
            if(find+1!=n):
                lhs=k*(high-mid+1)-(suffix_sum[mid]-suffix_sum[find+1])
            else:
                lhs=k*(high-mid+1)-(suffix_sum[mid]-suffix_sum[find])
            rhs=mid
            if(lhs==rhs):
                break
            elif(lhs<rhs):
                high=mid-1
            elif(lhs>rhs):
                low=mid+1 
            
        if(lhs<=rhs):
            count=n-mid
        else:
            count=ans
            
        print(count)
            
          


            
        
        
    
