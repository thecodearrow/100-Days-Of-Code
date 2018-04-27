#Trouble Sort

t=int(input())

def TSort(a):
    done=False
    while(not done):
        done=True
        for i in range(len(a)-2):
            if(a[i]>a[i+2]):
                done=False
                a[i],a[i+2]=a[i+2],a[i]
    check=True
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            check=False
            return i
    if(check==True):
        return -1 #positive!
        
for i in range(1,t+1):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    ans=TSort(arr)
    if(ans==-1):
        print("Case #"+str(i)+': OK')
    else:
        print("Case #"+str(i)+':',ans)
    