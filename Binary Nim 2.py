#https://www.codechef.com/problems/BINIM2

#https://www.youtube.com/watch?v=w6l_tDniL34&feature=youtu.be

t=int(input())

while t!=0:
    t-=1
    temp=input().split()
    p1="Dee" #0
    p2="Dum" #1
    start=temp[1]
    if(start==p1):
        start=0
    else:
        start=1
    n=int(temp[0])

    l=[]
    for i in range(n):
        s=input()
        s=list(s)[::-1] #stack
        s=[int(x) for x in s]
        l.append(s)
    
    
    
    
    while True:
        finished=False
        for s in l:
            done=False
            #playing optimally 
            while(s):
                if(s[-1]==start):
                    s.pop() 
                    done=True
                    finished=True
                else:
                    break
            if(done):
                break

               

        if(not finished):
            break
        start=1-start

    if(start==0):
        print("Dee")
    else:
        print("Dum")


