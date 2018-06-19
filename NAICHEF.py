from collections import defaultdict
t=int(input())

while(t!=0):
    t-=1 
    n,a,b=[int(x) for x in input().split()]
    dice=[int(x) for x in input().split()]
    dice_freq={}
    dice_freq=defaultdict(lambda:0,dice_freq)
    for d in dice:
        dice_freq[d]+=1 
    
    p1=dice_freq[a]/n
    p2=dice_freq[b]/n
    p=p1*p2 
    print("%.10f" % p)
        