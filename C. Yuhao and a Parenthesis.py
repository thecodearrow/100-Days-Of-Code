#http://codeforces.com/contest/1097/problem/C

import sys
import math
from collections import defaultdict


def getInputFromLine():
	return [int(x) for x in input().split()]

try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')

except: 
    pass


def mirror(s):
	s=s[::-1]
	m=""
	for c in s:
		if(c==")"):
			m+="("
		else:
			m+=")"
	return m

def getScore(s):
	score=0
	for b in s:
		if(b=="("):
			score+=1
		elif(b==")"):
			score-=1 

		if(score<0):
			return -1 

	return score

	
n=int(input())
brackets=[]
for i in range(n):
	t=input()
	brackets.append(t)
scores=[]
count=0

bal=defaultdict(lambda:0)

lead=0 #counting existing good brackets
for b in brackets:
	balance=getScore(b)
	if(balance!=-1):
		bal[balance]+=1

	if(balance==0):
		lead+=1
		


for b in brackets:
	m=mirror(b)
	balance=getScore(m)
	if(balance!=-1):
		if(bal[balance]>0):
			bal[balance]-=1
			count+=1
		

print(count-lead+(lead//2))