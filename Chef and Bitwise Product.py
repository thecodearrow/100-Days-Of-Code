#https://www.codechef.com/MAY20B/problems/CHANDF

#https://www.youtube.com/watch?v=-F7cHQ-gWS4  -- Video Explaination by Rachit Jain


import sys
import math
from collections import Counter,defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass
    
def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def takeInput():
    return [int(x) for x in input().strip().split()]
 
def F(x,y,z):
    return (x&z)*(y&z)


def calculatePossibleZ(x,y,l,r):
    possible_z=[]
    total_bits=42
    z=0
    idx=total_bits
    while idx>0:
        bit_at_l=l & (1<<idx)
        bit_at_r=r & (1<<idx)
        if(bit_at_l!=bit_at_r):
            break
        idx-=1

    start=idx #the index from which l and r are different
    #this bit in z can be set to 0 or 1
    z1=l #<r
    z2=r  #<l

    #All we need to ensure now is z1>L
    for i in range(start-1,-1,-1):
        bit_at_l=l & (1<<i)
        if(bit_at_l==0):   
	        #set this bit in z1 so as to ensure >L
	        z11=set_bit(z1,i)
	        for j in range(i-1,-1,-1):
	            #rest of the bits have to be X | Y 
	            bit_at_x=x & (1<<j)
	            bit_at_y=y & (1<<j)
	            if(bit_at_x | bit_at_y):
	                z11=set_bit(z11,j)
	            else:
	                z11=clear_bit(z11,j)

	        #print("z11",z11,bin(z11))
	        if(z11>=l and z11<=r):
	            possible_z.append(z11)

	        z1=clear_bit(z1,i)
        #do not set set this bit and see if you can find the next unset bit in l
    




    #All we need to ensure now is z2<R

    for i in range(start-1,-1,-1):
        bit_at_r=r & (1<<i)
        if(bit_at_r):
	        #don't set this bit in z2 so as to ensure <R
	        z22=clear_bit(z2,i)
	        for j in range(i-1,-1,-1):
	            #rest of the bits have to be X | Y 
	            bit_at_x=x & (1<<j)
	            bit_at_y=y & (1<<j)
	            if(bit_at_x | bit_at_y):
	                z22=set_bit(z22,j)
	            else:
	                z22=clear_bit(z22,j)
	        if(z22>=l and z22<=r):
	            possible_z.append(z22)
	        z2=set_bit(z2,i)  #set this bit and see if you can find the next set bit in r

    return possible_z


t=int(input())
while t!=0:
    #print()
    t-=1
    x,y,l,r=takeInput()
    max_f=-float("inf")
    possible_z=calculatePossibleZ(x,y,l,r)
    possible_z.append(l)
    possible_z.append(r) #l and r are valid possible z
    possible_z=sorted(possible_z) #since we need the smallest possible z for which Fmax is obtained
    #print(possible_z)
    ans=l
    for z in possible_z:
        current_f=F(x,y,z)
        if(current_f>max_f):
            max_f=current_f
            ans=z

    print(ans)

