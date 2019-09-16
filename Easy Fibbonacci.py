#Reference https://www.geeksforgeeks.org/program-find-last-digit-nth-fibonnaci-number/
# first 60 Fibonacci numbers since the pattern repeats

#https://www.codechef.com/SEPT19B/problems/FIBEASY

import math
def fibbo(f, n): 
    f[0] = 0; 
    f[1] = 1; 
    for i in range(2, n + 1): 
        f[i] = (f[i - 1] + f[i - 2]) % 10; 
    return f; 
  
def lastDigitFibbonacci(n): 
    f = [0] * 61
    f = fibbo(f, 60)
    return f[n % 60]

def floorLog(n):
    i=0
    while True:
        pow1=pow(2,i)
        pow2=pow(2,i+1)
        if(pow1<=n and n<pow2):
            return pow1
        else:
            i+=1
t=int(input())
while t!=0:
    t-=1
    n=int(input())
    survivor=floorLog(n) #nearest power of 2 floor
    print(lastDigitFibbonacci(survivor-1))
    