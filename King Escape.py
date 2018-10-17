
"""
https://codeforces.com/contest/1033/problem/A

Imagine a two-dimensional plane with origin positioned on the black queen. We notice that the queen partitions the board into up to four
 connected components, with each quadrant being one of them. The answer is thus "YES" if and only if the source king position and the target 
 position are in the same quadrant. 



The diagonal blocked states don't matter.

"""
n=int(input())
queen=[int(x) for x in input().split()]
king=[int(x) for x in input().split()]
dest=[int(x) for x in input().split()]

#shifting origin wrt to queen
def isSignSame(one,two):
	if(one>0 and two>0):
		return True
	if(one<0 and two<0):
		return True
	return False
king_new=[king[0]-queen[0],king[1]-queen[1]]
dest_new=[dest[0]-queen[0],dest[1]-queen[1]]


if(isSignSame(king_new[0],dest_new[0]) and isSignSame(king_new[1],dest_new[1])):
	print("YES")
else:
	print("NO")

"""

#Brute Force Graph BFS Solution times out! :( 

from collections import defaultdict 

class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)


    def BFS(self,start,dest):
        visited=defaultdict(lambda:False,{})
        visited[start]=True
        queue=[start]
        while queue:
            u=queue.pop(0)
            if(visited[dest]):
                return True
            for v in self.neighbours[u]:
                if(not visited[v]):
                    visited[v]=True
                    queue.append(v)

        return False




def positions(i,j,n,blocked):
    #check constraints and blocked states
    positions=[]
    x=i-1
    y=j-1
    if(x>0 and y>0 and (x,y) not in blocked):
        positions.append((x,y)) 

    x=i+1
    y=j+1
    if(x<n+1 and y<n+1 and (x,y) not in blocked):
        positions.append((x,y))  

    x=i-1
    y=j+1
    if(x>0 and y<n+1 and (x,y) not in blocked):
        positions.append((x,y))  

    x=i+1
    y=j-1
    if(x<n+1 and y>0 and (x,y) not in blocked):
        positions.append((x,y))  

    x=i 
    y=j+1
    if(y<n+1 and (x,y) not in blocked):
        positions.append((x,y))  

    x=i 
    y=j-1
    if(y>0 and (x,y) not in blocked):
        positions.append((x,y))  

    x=i-1 
    y=j
    if(x>0 and (x,y) not in blocked):
        positions.append((x,y))  

    x=i+1 
    y=j
    if(x<n+1 and (x,y) not in blocked):
        positions.append((x,y))  
    return positions

n=int(input())
queen=[int(x) for x in input().split()]
king=[int(x) for x in input().split()]
dest=[int(x) for x in input().split()]

blocked=set()

#rows and columns
for i in range(1,n+1):
    blocked.add((queen[0],i))
    blocked.add((i,queen[1]))



i=queen[0]
j=queen[1]
blocked.add((i,j))
while i>0 and j>0:
    i=i-1
    j=j-1
    blocked.add((i,j))

i=queen[0]
j=queen[1]

while i>0 and j<n+1:
    i=i-1
    j=j+1
    blocked.add((i,j))

i=queen[0]
j=queen[1]

while i<n+1 and j<n+1:
    i=i+1
    j=j+1
    blocked.add((i,j))
i=queen[0]
j=queen[1]


while i<n+1 and j>0:
    i=i+1
    j=j-1
    blocked.add((i,j))


g=Graph()
start=(king[0],king[1])
dest=(dest[0],dest[1])
queue=[start,dest]
visited=defaultdict(lambda:False)
while queue:
    u=queue.pop(0)
    i,j=u[0],u[1]
    moves=positions(i,j,n,blocked)
    for m in moves:
        if((i,j) not in blocked):
            g.addEdge((i,j),m)
        if(not visited[m]):
            visited[m]=True
            queue.append(m)


start=(king[0],king[1])
dest=(dest[0],dest[1])
if(g.BFS(start,dest) and start not in blocked):
    print("YES")
else:
    print("NO")






"""