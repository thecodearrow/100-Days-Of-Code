#Mishka and Contest Codeforces 999A

n,k=[int(x) for x in input().split()]

a=[int(x) for x in input().split()]


count=0

while(True):
    
    if(a[0]>k and a[-1]>k):
        break
    if(a[0]<=k):
        count+=1 
        del(a[0])
    if(len(a)==0):
        break
    if(a[-1]<=k):
        count+=1 
        del(a[-1])
    if(len(a)==0):
        break
        
print(count)
  

n=int(input())
s=input()

divisors=[]

for i in range(2,n//2+1):
    if(n%i==0):
        divisors.append(i)

d=s
for i in divisors:
    d=d[:i][::-1]+d[i:]
    
    
print(d[::-1])