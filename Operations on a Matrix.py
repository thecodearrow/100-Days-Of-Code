#https://www.codechef.com/OCT19B/problems/SAKTAN
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
    n,m,q=takeInput()
    row_val=[0]*n
    col_val=[0]*m
    for q_i in range(q):
        i,j=takeInput()
        row_val[i-1]+=1
        col_val[j-1]+=1
    ans=0
    
    odd_r=0
    even_r=0
    odd_c=0
    even_c=0
    for r in row_val:
        if(r%2==0):
            even_r+=1
        else:
            odd_r+=1

    for c in col_val:
        if(c%2==0):
            even_c+=1
        else:
            odd_c+=1
    #Odd number is the addition of one odd and one even
    print(even_r*odd_c+odd_r*even_c)


