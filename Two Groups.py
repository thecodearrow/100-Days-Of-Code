#https://www.codechef.com/problems/TWOGRS


import sys
import math
 
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
    a,b,c=takeInput()
    s=a+2*b+3*c 
    if(s%2!=0):
        print("NO") #Odd Sum can't be split
    else:
        

        #Greedily place as many as 1s,2s and 3s as possible into 2 sets
        while a>=40:
            a-=2
        while b>=40:
            b-=2
        while c>=40:
            c-=2

        remSum=(a+2*b+3*c)/2
        #For the remaining, use brute force and see if solution exists
        #Using atmost A 1s, atmost B 2s and atmost C 3s
        possible=False
        for i in range(a+1):
            for j in range(b+1):
                for k in range(c+1):
                    if(i+2*j+3*k==remSum):
                        possible=True
                        break

        if(possible):
            print("YES")
        else:
            print("NO")





