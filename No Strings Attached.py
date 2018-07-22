#https://www.codechef.com/JULY18B/problems/NSA
 
#Partially Solved 30 pts 

#Reference Counting Inversions 
#https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0  
import heapq
only={}
only[1]=True
def calculateY(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)/2]
        b = arr[len(arr)/2:]
        a, ai = calculateY(a)
        b, bi = calculateY(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
    	tiny=a[:]
    	heapq.heapify(tiny)
        if a[i] >= b[j]:
            c.append(a[i])
            heapq.heappop(tiny)
            i += 1
        else:
        	if(only[1]):
        		c.append(tiny[0])
        		print("derpa?")
        		only[1]=False
        		j += 1
        	else:
           		c.append(b[j])
            	inversions += (len(a)-i)
            	j += 1
            
            
    c += a[i:]
    c += b[j:]
    return c,inversions
 
t=int(raw_input())
for test in range(t):
	replace={}
	s=raw_input()
	n=len(s)
	new_string=list(s)
 	new_s,y=calculateY(new_string)
	print(new_s,y)
 


