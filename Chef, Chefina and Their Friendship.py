
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

def computerRollHash(s):
    #rolling hash array! 
    roll_hash=[0 for i in range(len(s))]
    roll_hash[0]=ord(s[0])-ord('a')+1
    p=31
    MOD=10**9+9
    power=[1]*n
    for i in range(1,len(s)):
        c=s[i]
        c_index=ord(c)-ord('a')+1
        roll_hash[i]=(c_index+(p*roll_hash[i-1]))%MOD
        power[i]=(power[i-1]*p)%MOD
        

    return roll_hash,power


def substrRollHash(l,r,roll_hash,power):
    #r excluded
    r-=1
    p=31
    MOD=10**9+9
    if(l==0):
        return roll_hash[r]
    substr_roll_hash=roll_hash[r]-(roll_hash[l-1]*power[r-l+1])
    return substr_roll_hash%MOD


t=int(input())
while t!=0:
    t-=1
    s=input()
    n=len(s)
    count=0
    roll_hash,power=computerRollHash(s) #
    for i in range(1,(len(s))):
        #break at i
        t11=substrRollHash(0,i//2,roll_hash,power)
        t12=substrRollHash(i//2,i,roll_hash,power)
        t21=substrRollHash(i,(i+n)//2,roll_hash,power)
        t22=substrRollHash((i+n)//2,n,roll_hash,power)
        if(t11==t12 and t21==t22):
            count+=1
    print(count)