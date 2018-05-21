
#CodeChef Cricket Score Problem Code: CRICSCR
n=int(input())
runs=[0]
wickets=[0]
valid=True
while(n!=0):
    n=n-1
    r,w=[int(x) for x in input().strip().split()]
    if(wickets[-1]==10 and r>runs[-1]): #ten wickets have fallen! MATCH OVERRR
        print("NO")
        valid=False
        break
        
    if(r<runs[-1] or w<wickets[-1] or w>10 ):
        print("NO")
        valid=False
        break
    
    runs.append(r)
    wickets.append(w)
    
if(valid):
    print("YES")