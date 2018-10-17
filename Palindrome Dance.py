
#http://codeforces.com/contest/1040/problem/A

n,white,black=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
left=0 
right=n-1 

impossible=False 
cost=0
while left<=right:
    ele1=a[left]
    ele2=a[right]
    if(ele1+ele2==1):
        impossible=True
        break 
    if(ele1==2 and ele2==2):
        cost+=min(white,black)
        if(left!=right):
            cost+=min(white,black)

    elif(ele1!=ele2):
        if(ele1+ele2==2):
            cost+=white 
        else:
            cost+=black
        
    left+=1
    right-=1

if(not impossible):
    print(cost)
else:
    print(-1)
    
    