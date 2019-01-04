#https://www.codechef.com/NOV18B/problems/PRDRG

#NOVEMBER LONG CHALLENGE 2018

#Take a paper and work the solution out ;) 

#n ranges from 1 to 25 only 

import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass



given=[int(x) for x in input().split()]

t=given[0]

fold={} #fold[k]=[numerator,denominator]


fold[1]=[1,2]  

for i in range(2,26):
    curr=[1,2**i] 
    prev=fold[i-1]
    store=[0,0]
    if(i%2==0): #subtract
        store[0]=prev[0]*2-curr[0]

    else:
        store[0]=prev[0]*2+curr[0]
        
    store[1]=2**i
    fold[i]=store

ans=[]
for i in range(1,t+1):
    ele=given[i]
    ans.append(fold[ele][0]) #num
    ans.append(fold[ele][1]) #denom

print(*ans)

