# PARTIALLY SOLVED

t=int(input())

while(t!=0):
    t=t-1
    n=int(input())
    influ=[int(x) for x in input().strip().split()]
    prefix=[0,0]
    for i in range(2,n):
        prefix.append(prefix[i-1]+influ[i-1])
    
    votes=[0]*n

    for i in range(n):
        for j in range(n):
            if(j>i):
                special=j
                other=i
            else:
                special=i
                other=j
            if(i!=j):
                if(influ[j]>=(prefix[special]-prefix[other+1])):
                    votes[i]=votes[i]+1
 
    for v in votes:
        print(v,end=' ')
    print()
