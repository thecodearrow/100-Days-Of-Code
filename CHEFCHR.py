"""
February long contest 2018
"""


t=int(input())

from itertools import permutations
while(t!=0):
    t=t-1
    s=input()
    chef_combi=list(permutations("chef"))
    chef_combi=[''.join(i) for i in chef_combi]
    index=0
    count=0
    while(index<=len(s)-4):
        current=s[index:index+4]
        index=index+1
        if(current in chef_combi):
            count=count+1
            
    
    if(count==0):
        print("normal")
    else:
        print("lovely",count)
    
    
