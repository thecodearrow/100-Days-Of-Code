
#https://www.facebook.com/hackercup/problem/2426282194266338/
import sys
try: 
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')

except: 
	pass


n=int(input())

for i in range(1,n+1):
    pond=input() 
    B=0
    dots=0
    for c in pond:
        if(c=="B"):
            B+=1
        if(c=="."):
            dots+=1

    if(B==0 or dots==0):
        print("Case #"+str(i)+": "+"N")
    else:
        if(dots<=B):
            print("Case #"+str(i)+": "+"Y")
        else:
            if(B>=2):
                print("Case #"+str(i)+": "+"Y")
            else:
                print("Case #"+str(i)+": "+"N")




		

		
				




		

