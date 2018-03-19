# March Challenge 2018 DIV 2

t=int(input())

while(t!=0):
    t=t-1
    n=int(input())
    fingers=[int(x) for x in input().strip().split()]
    sheath=[int(x) for x in input().strip().split()]
    sheathr=sheath[::-1]
    front=1
    back=1
    for i in range(n):
        if(fingers[i]>sheath[i]):
            front=0
            break
    for i in range(n):
        if(fingers[i]>sheathr[i]):
            back=0
            break
    
    if(front and back):
        print("both")
    elif(back):
        print("back")
    elif(front):
        print("front")
    else:
        print("none")
    
    