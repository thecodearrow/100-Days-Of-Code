#https://www.codechef.com/COOK119B/problems/CACHEHIT


import sys
import math
from collections import Counter,defaultdict
import heapq
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass
    


t=int(input())
while t!=0:
    t-=1
    n,b,m=[int(x) for x in input().split()]
    items=[int(x) for x in input().split()]
    cache={}
    current_cache=0
    for i in range(n):
        if(i%b==0):
            current_cache+=1
        cache[i]=current_cache

    current_cache=0
    cache_misses=0
    for b in items:
        if(cache[b]!=current_cache):
            current_cache=cache[b]
            cache_misses+=1
    print(cache_misses)



