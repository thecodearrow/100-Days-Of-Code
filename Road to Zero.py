#https://codeforces.com/contest/1342/problem/A
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
	x,y=takeInput()
	a,b=takeInput()
	ans=0
	x1,y1=abs(x),abs(y)
	ans1=b*min(x1,y1)+a*abs(x1-y1)
	ans2=a*(x1+y1)
	print(min(ans1,ans2))