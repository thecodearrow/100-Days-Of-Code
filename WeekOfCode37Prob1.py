import os
import sys
import math
import re
# Complete the averageOfTopEmployees fuhanction below.
def digitRipper(n):
    s=str(n)
    g=re.search('\.[\d]{1}',s)
    deci=g.group()
    decider=deci[1]
    return int(decider)
    
    
def averageOfTopEmployees(rating):
    bonus=[]
    for r in rating:
        if r>=90:
            bonus.append(r)
    
    avg=sum(bonus)/len(bonus)
    avg=avg*100
    if(isinstance(avg, float)):
        d=digitRipper(avg)
        if(d>=5):
            avg=math.ceil(avg)
        else:
            avg=math.floor(avg)
        
    avg=avg/100
    print("%.2f"%avg)

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)