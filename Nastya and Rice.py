#https://codeforces.com/contest/1341/problem/A

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
    n,a,b,c,d=takeInput()
    min_weight=(a-b)*n 
    max_weight=(a+b)*n
    found=True
    #print(min_weight,max_weight,c-d,c+d)
    if(max_weight<c-d or min_weight>c+d):
        found=False
    
    if(found):
        print("Yes")
    else:
        print("No")



