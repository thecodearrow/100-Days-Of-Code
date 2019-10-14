#https://www.codechef.com/OCT19B/problems/MSNG/
import sys
from collections import defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 


def anyBaseToTen(s,base):
    try:
        value=int(s,base)
        if(value>pow(10,12)):
            return -1
        return value

    except:
        return -1

def takeInput():
    return [x for x in input().strip().split() ]
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    numbers=[]
    some_base_present=False
    for i in range(n):
        base,value=input().strip().split()
        base=int(base) 
        if(base!=-1):
            some_base_present=True

        numbers.append([base,value])

    values=[set() for i in range(n)]
    for i in range(n):
        base,string=numbers[i]
        for b in range(2,37):
            if(base==-1):
                value=anyBaseToTen(string,b)
            else:
                value=anyBaseToTen(string,base)

            if(value!=-1):
                values[i].add(value)

    
    first_set=sorted(list(values[0]))
    common_element_found=False
    #Search for common elements for all values found and print smallest
    for ele in first_set:
        present=[False for i in range(n)]
        for i in range(n):
            if(ele in values[i]):
                present[i]=True

        false_found=False
        for bool_value in present:
            if(not bool_value):
                false_found=True
                break
            
        if(not false_found):
            print(ele)
            common_element_found=True
            break
            
    if(not common_element_found):
        print(-1)
            
            
        















