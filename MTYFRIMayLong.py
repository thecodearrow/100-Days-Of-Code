t=int(input())
while(t!=0):
    t=t-1
    n,k=[int(x) for x in input().strip().split()]
    a=[int(x) for x in input().strip().split()]
    motu=[]
    tomu=[]
    sum_m=0
    sum_t=0
    for i in range(n):
        if(i%2==0):
            motu.append(a[i]) 
            sum_m+=a[i]
        else:
            tomu.append(a[i])
            sum_t+=a[i]
            
    if(sum_t>sum_m):
        print("YES")
    else:
        motu=sorted(motu)
        tomu=sorted(tomu)
        last=-1
        first=0
        wins=False
        for i in range(k):
            if(not tomu or not motu): #empty list
                break
            sum_t-=tomu[first]
            sum_t+=motu[last]
            sum_m+=tomu[first]
            sum_m-=motu[last]
            del(tomu[first])
            del(motu[last])
            if(sum_t>sum_m):
                print("YES")
                wins=True
                break
        if(not wins):
            print("NO")
