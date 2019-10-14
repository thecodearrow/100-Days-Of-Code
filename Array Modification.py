#https://www.codechef.com/OCT19B/problems/MARM

import sys

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 

def takeInput():
    return [int(x) for x in input().strip().split()]
 

t=int(input())
while t!=0:
    t-=1
    n,k=takeInput()
    a=takeInput()
    if(k>=n):
        if(n%2!=0):
            #Edge case when n is odd 
            #The middle element becomes zero!
            mid=(n//2)
            a[mid]=0
    k=k%(3*n) #Pattern Repeats after 3*n
    for i in range(k):
        one=a[i%n]
        two=a[n-(i%n)-1]
        a[i%n]=one^two
    print(*a)


