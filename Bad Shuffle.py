#https://www.codechef.com/SEPT18A/problems/BSHUFFLE

#https://getpocket.com/a/read/560859201


n=int(input())
print1=[] #most favorable
print2=[n] #least favorable
add=n//2   

for i in range(2,n+1):
    print1.append(i)
    
print1.append(1)
mid=n//2 
if(n%2==0):
    mid=mid-1

print1[mid],print1[n-1]=print1[n-1],print1[mid]
    
for i in range(1,n):
    print2.append(i)
    
print(*print1)
print(*print2)

"""TESTING


import random
from collections import defaultdict
def randomize(n):
	num=[]
	for i in range(n):
		num.append(i)

	for i in range(n):
		idx1=i
		idx2=random.randrange(0,n)
		num[idx1],num[idx2]=num[idx2],num[idx1]


	return num 

def cleanup(a1,a2):
    a1=a1.replace("[","")
    a1=a1.replace("]","")
    a2=a2.replace("[","")
    a2=a2.replace("]","")
    a1=a1.split(",")
    a2=a2.split(",")
    a1=[int(x) for x in a1]
    a2=[int(x) for x in a2]
    return a1,a2
n=int(input())
freq=defaultdict(lambda:0)
limit=300000
for i in range(limit):
	p=str(randomize(n))
	freq[p]+=1


ans1=[]
ans2=[]

for i in range(n):
	ans1.append(i)
	ans2.append(i)
ans1=str(ans1)
ans2=str(ans2)

for item in list(freq):
	if(freq[item]>=freq[ans1]):
		ans1=item 
	if(freq[item]<=freq[ans2]):
		ans2=item 
print1,print2=cleanup(ans1,ans2)
print2

for p in print1:
    print(p+1,end=' ')

print()
print2=[n-1]
for i in range(n-1):
    print2.append(i)
for p in print2:
    print(p+1,end=' ')




"""