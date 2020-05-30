#https://www.codechef.com/COOK118B/problems/CHFIMPRS/

import sys
import math
from collections import Counter,defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass
    

def takeInput():
    return [int(x) for x in input().strip().split()]


t=int(input())
while t!=0:
    t-=1
    n,m=takeInput()
    matrix=[]
    for i in range(n):
        row=takeInput()
        matrix.append(row)

    count=defaultdict(lambda:0)
    for i in range(n):
        for j in range(m):
            count[matrix[i][j]]+=1


    new=[[0 for i in range(m)]for j in range(n)]

    
    evens=[]
    heapq.heapify(evens)
    for c in count:
        heapq.heappush(evens,[-count[c],c])

    for i in range(n):
        start=0
        end=m-1
        while start<end:
            if(not evens):
                possible=False
                break
            even_char_count,even_char=heapq.heappop(evens)
            even_char_count*=-1
            if(even_char_count<2):
                possible=False
                break
            count[even_char]-=2
            new[i][start]=even_char
            new[i][end]=even_char
            if(count[even_char]>0):
                heapq.heappush(evens,[-count[even_char],even_char])
            start+=1
            end-=1
    if(m%2!=0):
        mid=m//2
        odd=evens
        for i in range(n):
            if(not odd):
                possible=False
                break
            odd_char_count,odd_char=heapq.heappop(evens)
            count[odd_char]-=1
            new[i][mid]=odd_char
            if(count[odd_char]>0):
                heapq.heappush(odd,[-count[odd_char],odd_char])

    possible=True
    for i in range(n):
        if(not possible):
            break
        for j in range(m):
            if(new[i][j]==0):
                possible=False
                break

    if(possible):
        for i in range(n):
            print(*new[i])
    else:
        print(-1)


