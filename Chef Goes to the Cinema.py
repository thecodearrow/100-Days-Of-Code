#Chef Goes to the Cinema Problem Code: CO92SUBW

"""

Chef lives in Chefcity. Chefcity can be represented as a straight line with Chef's house at point 0 on this line. There is an infinite number of subway stations in Chefcity, numbered by positive integers. The first station is located at point 1 and for each i ≥ 1, the distance between stations i and i+1 is equal to i+1. (Station i+1 is always located at a higher coordinate than station i, i.e., the subway stations are located at points 1, 3, 6, 10, 15 etc.)

Subway trains in Chefcity allow Chef to move between any pair of adjacent stations in one minute, regardless of the distance between them. Chef can also move by walking; his walking speed is one unit of distance in one minute. Chef can enter or exit the subway at any station.

Chef has decided to go to the cinema. The only cinema in Chefcity is located at point X. (Note that the cinema can be placed at the same point as a subway station.) Help Chef determine the minimum possible time required to get to the cinema from his house.


"""

def subslessthanN(N):
    stations=[1]
    i=0
    k=2
    while(stations[i]<=N):
        stations.append(stations[i]+k)
        i=i+1
        k=k+1
        
    stations.append(stations[i]+k)
    return(stations)
 
import numpy as np
 
 
t=int(input())
 
while(t!=0):
    t=t-1
    x=int(input())
    subs=subslessthanN(x)
    index=np.searchsorted(subs,x)
    time=1
    if(subs[index]==x):
        time=time+index
    else:
        one=time+index-1+abs(subs[index-1]-x)
        two=time+index+abs(x-subs[index])
        right=min(one,two)
        time=right
    print(time)