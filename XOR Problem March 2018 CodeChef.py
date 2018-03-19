# cook your dish here
import numpy as np
 
def compli(b):
    #function that computes bitwise not
    b=b[2:]
    compliment=""
    for c in b:
        if(c=='0'):
            compliment=compliment+"1"
        else:
            compliment=compliment+"0"
   
    return(compliment)
 
temp=[int(x) for x in input().strip().split()]
n=temp[0]
q=temp[1]
values=[int(x) for x in input().strip().split()]
compliments=[]
for i in values:
    compliments.append(compli(bin(i)))
 
common_length=len(max(compliments,key=len))
compliments2=[] #making sure all are of the same length of common_length
 
for c in compliments:
    to_add='1'*(common_length-len(c))
    c=to_add+c 
    compliments2.append(c)
 
 
compliments2=[list(x) for x in compliments2]
compliments2=np.array(compliments2).astype(int).tolist()  
prefixsum=np.cumsum(compliments2,axis=0)
 
while(q!=0):
    q=q-1
    temp=[int(x) for x in input().strip().split()]
    start=temp[0]
    end=temp[1]
    answer=""
    length=(end-start)+1
    sum_bits=[]
    decider=(length+1)//2
    if(start==1):
      L=[0]*common_length
      R=prefixsum[end-1]
    else:
      L=prefixsum[start-2]
      R=prefixsum[end-1]
    sum_bits=(R-L).tolist()
     
    for b in sum_bits:
        if(length%2==0):
            if(b<=decider):
                answer=answer+'0'
            else:
                answer=answer+'1'
        else:
            if(b<decider):
                answer=answer+'0'
            else:
                answer=answer+'1'
    answer='1'*(31-len(answer))+answer
    print(int(answer,2))  
