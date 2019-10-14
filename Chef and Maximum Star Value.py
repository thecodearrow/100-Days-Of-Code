#https://www.codechef.com/OCT19B/problems/MSV/

#AC PyPy3
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
    a=takeInput()
    ans=0
    limit=max(a)
    freq=[0]*10**6
    for ele in a:
        freq[ele]+=1

    for i in range(n-1,-1,-1):
        ele=a[i]
        if(ans>=i):
            #ans >= max possible at index i, we can stop search
            break
        star_value=0
        for j in range(2*ele,limit+1,ele):
            #All multiples of current ele
            if(freq[j]>0):
                star_value+=freq[j]
        freq[ele]-=1 #Excluding the current element since search is complete!
        star_value+=freq[ele] #other repeats of current element in the left part of array
        ans=max(star_value,ans)



    print(ans)

