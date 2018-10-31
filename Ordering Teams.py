#https://www.codechef.com/TSTIND18/problems/ORDTEAMS


"""
In ACM-ICPC contests, there are usually three people in a team. For each person in the team, you know their scores in three skills - hard work, intelligence and persistence.

You want to check whether it is possible to order these people (assign them numbers from 1 to 3) in such a way that for each 1 ≤ i ≤ 2, i+1-th person is stricly better than the i-th person.

A person x is said to be better than another person y if x doesn't score less than y in any of the skills and scores more than y in at least one skill.

Determine whether such an ordering exists.

"""

#https://www.codechef.com/problems/BINIM2

import sys
from collections import defaultdict


try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass


def better(x,y):
    #is x better than y
    if(x[0]>=y[0] and x[1]>=y[1] and x[2]>=y[2]):
        if(x[0]>y[0] or x[1]>y[1] or x[2]>y[2]):
            return True 
        else:
            return False 

    return False


t=int(input())

while t!=0:
    t-=1
    p1=[int(x) for x in input().split()]
    p2=[int(x) for x in input().split()]
    p3=[int(x) for x in input().split()]
    one=[]
    two=[]
    three=[]
    if(better(p1,p2)):
        one.append(1)
    else:
        one.append(0)

    if(better(p1,p3)):
        one.append(1)
    else:
        one.append(0)

    if(better(p2,p1)):
        two.append(1)
    else:
        two.append(0)

    if(better(p2,p3)):
        two.append(1)
    else:
        two.append(0)


    if(better(p3,p1)):
        three.append(1)
    else:
        three.append(0)

    if(better(p3,p2)):
        three.append(1)
    else:
        three.append(0)

    
    if(one[0] and one[1]):
        if(two[1] or three[1]):
            print("yes")
        else:
            print("no")
    elif(two[0] and two[1]):
        if(three[0] or one[1]):
            print("yes")
        else:
            print("no")
    elif(three[0] and three[1]):
        if(one[0] or two[0] ):
            print("yes")
        else:
            print("no")
    else:
        print("no")

