#https://codeforces.com/contest/1342/problem/B

import sys
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline 
    
 
def takeInput():
    return [int(x) for x in input().strip().split()]
 
        
t=int(input())
while t!=0:
	t-=1
	s=input()
	if('0' in s and '1' in s):
		if(s[0]=='0'):
			ans='01'*(len(s))
		else:
			ans='10'*(len(s))
	else:
		ans=s
	print(ans)