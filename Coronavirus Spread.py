#https://www.codechef.com/MAY20B/problems/COVID19

# cook your dish here


import sys
import math
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass
    


def takeInput():
    return [int(x) for x in input().strip().split()]
 
        

t=int(input())
while(t!=0):
    t-=1
    n=int(input())
    A=takeInput()
    min_chain,max_chain=float("inf"),-float("inf")
    l=1
    for i in range(1,n):
        diff=abs(A[i]-A[i-1])
        if(diff<=2):
            l+=1
        else:
            min_chain=min(min_chain,l)
            max_chain=max(max_chain,l)
            l=1
    min_chain=min(min_chain,l)
    max_chain=max(max_chain,l)
    print(min_chain,max_chain)
    

            


        

    
