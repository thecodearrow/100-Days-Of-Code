#https://codeforces.com/contest/1221/problem/A

import sys
import math
from collections import defaultdict
 
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 
 
 
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    store=set()
    for ele in a:
        store.add(ele)
    if(2048 in store):
        print("YES")
    else:
        store=set()
        found=False
        for ele in a:
            if(ele not in store):
                store.add(ele)
            else:
                new_ele=ele 
                while new_ele in store:
                    store.remove(new_ele)
                    new_ele=new_ele*2 
                if(new_ele==2048):
                    found=True
                    break
                store.add(new_ele)
        if(found):
            print("YES")
        else:
            print("NO")