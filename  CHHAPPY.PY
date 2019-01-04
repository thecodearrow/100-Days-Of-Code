#https://www.codechef.com/NOV18B/problems/CHHAPPY


import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass

t=int(input())


"""
1. Create a dict of repeatting elements as key and their indices as values stored as a list
2.Iterate over the dict and check if atleast two of the indices occur as elements in the array
3.DONE.

"""

from collections import defaultdict
def goodsequence(a):
    there=set()

    for ele in a:
        there.add(ele)

    repeats=defaultdict(list)

    for i in range(1,len(a)+1):
        ele=a[i-1]
        repeats[ele].append(i)

    for val in repeats:
        if(len(repeats[val])>=2):
            count=0
            for idx in repeats[val]:
                if(idx in there):
                    count+=1
            if(count>=2):
                return True 

    return False
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]

    if(goodsequence(a)):
        print("Truly Happy") 
    else:
        print("Poor Chef")
   