#https://www.codechef.com/OCT19B/problems/S10E/

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
    n=int(input())
    prices=takeInput()
    ans=0
    for i in range(n):
        current_price=prices[i]
        good=True
        for j in range(1,6):
            if(i-j>=0):
                prev_price=prices[i-j]
                if(prev_price<=current_price):
                    good=False
                    break

        if(good):
            ans+=1

    print(ans)

