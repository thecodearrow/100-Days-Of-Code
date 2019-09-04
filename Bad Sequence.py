#http://codeforces.com/contest/1214/problem/C

n=int(input())
b=input()
stack=[]
c1=0
c2=0
for c in b:
    if(c=="("):
        c1+=1
    else:
        c2+=1
 
for c in b:
    if(c=="("):
        stack.append(c)
    if(c==")"):
        if(stack):
            stack.pop()
if(n%2==0):
    if(c1!=c2):
        print("No")
    elif(len(stack)>1):
        print("No")
    else:
        print("Yes")
else:
    print("No")