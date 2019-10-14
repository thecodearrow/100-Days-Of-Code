#https://www.codechef.com/OCT19B/problems/EVEDG

import sys
from collections import defaultdict
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    input = sys.stdin.readline
 


class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
        self.degree=defaultdict(lambda:0)

    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.degree[u]+=1
        self.neighbours[v].append(u)
        self.degree[v]+=1



    def BFS(self,source,visited):
        queue=[source]
        visited[source]=True
        sum_degree=0
        group=[]
        while queue:
            u=queue.pop(0)
            sum_degree+=self.degree[u]
            group.append(u)
            for v in self.neighbours[u]:
                if(not visited[v]):
                    visited[v]=True
                    queue.append(v)
        edge_count=int(sum_degree//2)
        return edge_count,group



def takeInput():
    return [int(x) for x in input().strip().split()]

t=int(input())
while t!=0:
    t-=1
    n,m=takeInput()
    partition=defaultdict(lambda:1)
    g=Graph()
    for i in range(m):
        u,v=takeInput()
        g.addEdge(u,v)
    degree=g.degree
    neighbours=g.neighbours

    if(m%2==0):
        k=1
    else:
        k=2
        groups_with_even_edges=[]
        groups_with_odd_edges=[]
        visited=defaultdict(lambda:False)
        for i in range(1,n+1):
            if(not visited[i]):
                edge_count,group=g.BFS(i,visited)
                if(edge_count%2!=0):
                    groups_with_odd_edges.append(group)
                else:
                    if(len(group)>1):
                        groups_with_even_edges.append(group)


        
        if(len(groups_with_even_edges)>0):
            #If there is a group with even edge count 
            #Convert it to odd edge count by removing one node with odd degree! (if possible!)
            solved=False
            for g in groups_with_even_edges:
                if(solved):
                    k=2
                    break
                for node in g:
                    if(degree[node]%2!=0):
                        #odd degree
                        partition[node]=2
                        solved=True
                        break

            
                    
        #If only odd edged groups are present
        #Try removing a odd degree node to make that group even edged!

        if(len(groups_with_even_edges)==0 or not solved):
            k=2
            solved=False
            for g in groups_with_odd_edges:
                if(solved):
                    break
                for node in g:
                    if(degree[node]%2!=0):
                        #odd degree
                        partition[node]=2
                        solved=True
                        break

            
            if(not solved):
                k=3
                #If no odd degree node can be removed
                #Two adjacent nodes must be removed

                #Separate two nodes out and keep them in seperate groups
               
                g=groups_with_odd_edges[-1]
                for g in groups_with_odd_edges:
                    if(solved):
                        break
                    for node1 in g:
                        if(solved):
                            break
                        for node2 in neighbours[node1]:
                            solved=True
                            partition[node1]=2
                            partition[node2]=3
                            break
               

                


    answer=[] 
    for i in range(1,n+1):
        answer.append(partition[i])
        
    print(k)
    print(*answer)







            











