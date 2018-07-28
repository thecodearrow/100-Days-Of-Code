#https://www.codechef.com/COOK96B/problems/ENCMSG/

#July Cook-Off 2018 Division 2  » Encoding Message

t=int(input())
while t!=0:
    t-=1
    n=int(input())
    s=input()
    message=list(s)
    if(n%2!=0):
        n-=1
    for i in range(1,n,2):
        message[i],message[i-1]=message[i-1],message[i]
 
    for i in range(len(message)):
        c=message[i]
        idx=ord(c)-96
        c1=chr(123-idx)
        message[i]=c1
 
    for i in message:
        print(i,end='')
 
    print()
 