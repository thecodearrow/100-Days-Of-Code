
#https://www.codechef.com/JULY18B/problems/GEARS
#Partially Solved PyPy 

from collections import defaultdict 
from fractions import Fraction
 
def convertF(d):
	return Fraction(d).limit_denominator()
 
n,m=[int(x) for x in raw_input().split()]
gears=[int(x) for x in raw_input().split()]
 
class Graph:
	def __init__(self):
		self.nextgear=defaultdict(list)
		self.blocked=defaultdict(lambda:False) 
		self.speed_gear={} 
 
	def addGear(self,u,v):
		self.nextgear[u].append(v)
		self.nextgear[v].append(u)
 
	def BFS(self,s,d,speed):
		visited=defaultdict(lambda:False,{})
		visited[s]=True 
		queue=[s]
		self.speed_gear[s]=Fraction(speed)
		while queue:
			u=queue.pop(0)
			if(visited[d]):
				ans=self.speed_gear[d]
				string=str(ans.numerator)+'/'+str(ans.denominator)
				return string
			for v in self.nextgear[u]:
				if(self.blocked[v]):
					return False
				if(not visited[v]):
					visited[v]=True
					dec=(-self.speed_gear[u])*Fraction(gears[u],gears[v])
					self.speed_gear[v]=convertF(dec)
					queue.append(v)
		return False
 
	def checkForCycles(self,g1):
		#if there is a odd cycle, block all gears in that cycle 
		queue=[g1]
		colored=defaultdict(lambda:False,{})
		colored[g1]=0
		cycle=False
		
		while(queue):
			u=queue.pop(0)
			for v in self.nextgear[u]:
				if(colored[v]==False):
					colored[v]=colored[u]^1
					queue.append(v)
				elif(colored[v]==colored[u]):
						cycle=True
						break
				
 
		if(cycle):
			queue=[g1]
			visited=defaultdict(lambda:False,{})
			visited[g1]=True 
			self.blocked[g1]=True
			while queue:
				u=queue.pop(0)
				for v in self.nextgear[u]:
					if(not visited[v]):
						visited[v]=True
						queue.append(v)
						self.blocked[v]=True
 
 
g=Graph()
for q in range(m):
	temp=[int(x) for x in raw_input().split()]
	if(temp[0]==1):
		i=temp[1]-1 
		val=temp[2] 
		gears[i]=val #changed value of gear i 
	elif(temp[0]==2):
		g1=temp[1]-1
		g2=temp[2]-1
		g.addGear(g1,g2)
		g.checkForCycles(g1)
 
	elif(temp[0]==3):
		#print gear2's speed 
		gear1=temp[1]-1
		gear2=temp[2]-1 
		speed=temp[3]
		connected=g.BFS(gear1,gear2,speed)
		if(not connected):
			print(0)
		else:
			print(connected)   