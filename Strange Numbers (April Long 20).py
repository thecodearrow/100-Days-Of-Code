#https://www.codechef.com/APRIL20B/problems/STRNO

import sys
import math

from collections import defaultdict
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	input = sys.stdin.readline #Python Fast I/O
	


import math as mt

def canNK(n, k): 

	#Can N be formed as a product of K numbers
    a = []
    while n % 2 == 0: 
        a.append(2) 
        n = n // 2
          
    for i in range(3, int(mt.sqrt(n))+1, 2): 
        while n % i == 0: 
            n = n / i; 
            a.append(i) 
              
    if n > 2: 
        a.append(n) 
          
    if len(a) < k: 
       return False

    return True
 


def takeInput():
    return [int(x) for x in input().strip().split()]
 
t=int(input())
while t!=0:
	t-=1
	n,p=takeInput()
	if(not canNK(n,p)):
		print(0)
	else:
		print(1)
		
