#https://www.codechef.com/APRIL20B/problems/ANSLEAK

import sys
import math
from collections import Counter
import random
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	input = sys.stdin.readline #Python Fast I/O
	


def takeInput():
    return [int(x) for x in input().strip().split()]
 

def mode(row):
	#Gives you a score of 75
	items=Counter(row)
	item_max_count=0
	ans=None
	for key in items:
	    if item_max_count<=items[key]:
	        ans=key
	        item_max_count=items[key]
	return ans

def weights(row):
	#Random Choices gives you a score fo 77 WTF! 
	freq=Counter(row)
	weights=[]
	for ele in row:
		weights.append(freq[ele])
	return weights


def weighted_mean(row):
	#Gives you a score of 50
	freq=Counter(row)
	s=0
	n=0
	for ele in freq:
		s+=(freq[ele]*ele)
		n+=freq[ele]

	mean=round(s/n)
	return round(mean)

def median(row):
	row=sorted(row)
	central_index=len(row)//2
	return row[central_index]

t=int(input())
while t!=0:
	t-=1
	q,c,n=takeInput()
	answers=[]
	for i in range(q):
		answers.append(takeInput())

	
	for i in range(q):
		print(random.choices(answers[i],weights=weights(answers[i]))[0],end=" ")
	print()
	
		
	


	




	
		
