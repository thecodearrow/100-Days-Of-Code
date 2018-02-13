"""
You are playing a revised version of the game, where, you have to unlock all doors in a given setting, in a given fashion, to enter the playig area.

Initially, any door is either locked or unlocked.
If a door is locked and you unlock it, then
if the next consecutive door is locked, it will automatically get unlocked.
if the next consecutive door is already unlocked, nothing will happen.
there will be no effect on any following door.
For example, if there are  doors as shown below, where  denotes an unlocked door, and  denotes a locked door, a minimum of  operations, will be required to unlock all doors.

Complete the function revisedRussianRoulette that takes an integer array denoting status of each door in the array, and return an integer array denoting the minimum and maximum number of unlock operations needed to unlock all the doors.
"""

import sys

def revisedRussianRoulette(doors):
    # Complete this function
    minCount=0
    maxCount=0
    for i in range(len(doors)):
        if(doors[i]==1):
            maxCount=maxCount+1
    for i in range(len(doors)):
        if(doors[i]==1):
            doors[i]=0
            minCount=minCount+1
            if(not i+1==len(doors) and doors[i+1]==1):
                doors[i+1]=0
                
    return(str(minCount)+" "+str(maxCount))
if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (result)