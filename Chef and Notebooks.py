
#https://www.codechef.com/FLMOCK02/problems/CNOTE

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
    a,b,money,n=[int(x) for x in input().split()]
    needed=a-b
    lucky=False
    for i in range(n):
        pages,cost=[int(x) for x in input().split()]
        if(cost<=money):
            if(pages>=needed):
                lucky=True 

    if(lucky):
        print("LuckyChef")
    else:
        print("UnluckyChef")

