#https://www.codechef.com/MAY20B/problems/CORUS



import sys
import math
from collections import Counter,defaultdict
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
    n,q=takeInput()
    s=input()
    count=Counter(s)
    queue=defaultdict(lambda:0)
    for c in count:
        if(count[c]!=1):
            queue[count[c]]+=1

    for _ in range(q):
        c=int(input())
        if(c==0):
            print(n)
        else:
            temp_queue=defaultdict(lambda:0,queue)
            to_add_later=[] #updated queue
            for item in queue.keys():
                if(item-c>=1):
                    to_add_later.append((item-c,temp_queue[item]))
                temp_queue[item]=0
            for key,val in to_add_later:
                temp_queue[key]=val
            ans=0
            for s in temp_queue:
                ans+=(temp_queue[s]*s)
            print(ans)









            


        

    
