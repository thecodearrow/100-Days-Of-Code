#https://www.codechef.com/FLPAST01/problems/MAY19F1

t=int(input())
while t!=0:
    t-=1
    n,q=[int(x) for x in input().split()]
    scores=[int(x) for x in input().split()]
    queries=[int(x) for x in input().split()]
    highest_at={}
    current_max=scores[0]
    for i,s in enumerate(scores):
        current_max=max(current_max,s)
        highest_at[i+1]=current_max
    for q in queries:
        print(highest_at[q])
