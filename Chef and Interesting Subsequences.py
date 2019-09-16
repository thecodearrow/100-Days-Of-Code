#https://www.codechef.com/SEPT19B/problems/CHEFINSQ

from collections import defaultdict
def numWays(i,a,target,sequence,k,n,memo):
    key=str(target)+":"+str(i)+":"+str(len(sequence))
    if(key in memo):
        return memo[key]
    if(len(sequence)==k):
        if(target==0):
            return 1
        else:
            return 0
    if(i>=n):
        return 0
    
    if(a[i]<=target):
        memo[key]=numWays(i+1,a,target-a[i],sequence+[a[i]],k,n,memo)+numWays(i+1,a,target,sequence,k,n,memo)
    else:
        memo[key]=numWays(i+1,a,target,sequence,k,n,memo)
    return memo[key]
t=int(raw_input())
while t!=0:
    t-=1
    n,k=[int(x) for x in raw_input().split()]
    a=[int(x) for x in raw_input().split()]
    a_min=sorted(a)[:k]
    target=sum(a_min)
    a_min=set(a_min)
    new_a=[]
    for ele in a:
        if(ele in a_min):
            new_a.append(ele)
    
    print(numWays(0,new_a,target,[],k,len(new_a),{}))
