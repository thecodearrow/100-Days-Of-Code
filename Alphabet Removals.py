#Codeforces 999C Div 3

from collections import defaultdict
n,k=[int(x) for x in input().split()]

s=input()

freq=[]
index=0 
for ele in s:
	freq.append([ele,index])
	index+=1 

#sorting it in alphabetical order

freq=sorted(freq) 

#remove the first k entries 

freq=freq[k:]

#sort entries based on index 

freq=sorted(freq,key=lambda x:x[1])

for entry in freq:
	print(entry[0],end='') 
