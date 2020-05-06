
#https://codeforces.com/contest/1348/problem/A
import math
def takeInput():
    return [int(x) for x in input().strip().split()]
 
        
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    c1=pow(2,n)
    c2=0
    half=n//2
    for i in range(1,half):
        c1+=pow(2,i)
    for i in range(half,n):
        c2+=pow(2,i)
    print(c1-c2)