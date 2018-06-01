#Codeforces Round 196 (Div. 2)

n,m=[int(x) for x in input().split()]
puzzles=[int(x) for x in input().split()]
puzzles=sorted(puzzles)
minimum=10**9+7 #infinity

for k in range(m-n+1):
    val=puzzles[k+n-1]-puzzles[k]
    minimum=min(minimum,val)
    
if(m==n):
    print(puzzles[-1]-puzzles[0])
else:
    
    print(minimum)