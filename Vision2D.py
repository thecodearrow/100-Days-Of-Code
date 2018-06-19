#AC for 2-D geometry! :)


import math
import numpy as np
 
t=int(input())
 
 
def distance(a,b):
    x=(a[0]-b[0])**2 
    y=(a[1]-b[1])**2 
    return(math.sqrt(x+y))
    
def pairTangents(xp,yp,h,k,r):
    tangents=[]
    a=(h-xp)**2-r**2
    b=2*(h-xp)*(yp-k)
    c=(yp-k)**2-r**2 
    d=b**2-4*a*c 
    if(a==0):
        tangents=["inf","inf"]
    else:
        m1 = (-b-math.sqrt(d))/(2*a)
        m2 = (-b+math.sqrt(d))/(2*a)
        tangents=[m1,m2]
    
    return tangents
        
while(t!=0):
    t-=1 
    px,py,pz,q0x,q0y,q0z,dx,dy,dz,cx,cy,cz,r=[int(x) for x in input().split()]
    
    tang=pairTangents(px,py,cx,cy,r)
    eqns=[] #equations for pair of tangents from an external point  
    
    
    if(tang[0]=="inf"):
        eqns.append([1,0,px])  #x=xp 
        slope=(r**2-(py-cy)**2)/(2*(cx-px)*(py-cy))
        m1=slope
        eqns.append([m1,-1,m1*px-py]) 
    else:
        m1=tang[0]
        m2=tang[1]
        eqns.append([m1,-1,m1*px-py])
        eqns.append([m2,-1,m2*px-py])
        
        
    #equation of q line connecting two points x1,y1 and x2,y2 
    
    x1=q0x 
    y1=q0y 
    
    x2=x1+dx
    y2=y1+dy 
    
    q_eqn=[]
    
    if(x2-x1==0):
        q_eqn=[1,0,x1]
    else:
        m=(y2-y1)/(x2-x1)
        q_eqn=[m,-1,m*x1-y1]
        
    
    #finding the intersection b/w pair of tangents and q line 
    
    
    soln=[]
    #tang 0 and q line 
    
    a = np.array([[eqns[0][0],eqns[0][1]], [q_eqn[0],q_eqn[1]]])
    b = np.array([eqns[0][2],q_eqn[2]])
    try:
        soln.append(np.linalg.solve(a, b).tolist())
    except:
        pass
    
    
    #tang 1 and q line 
    
    a = np.array([[eqns[1][0],eqns[1][1]], [q_eqn[0],q_eqn[1]]])
    b = np.array([eqns[1][2],q_eqn[2]])
    try:
        soln.append(np.linalg.solve(a, b).tolist())
    except:
        pass
    
    
    #final step finding t value 
    d=[dx,dy]
    q=[q0x,q0y]
    
    
    bag=[]        
    drandom=[x2,y2] #a random point on q line 
   
    min_d=10**10+7 # a very large value
    
 
    time=[]
    
    for s in soln:
        for i in range(2):
            if(d[i]!=0):
                temp=(s[i]-q[i])/d[i]
                time.append(temp)
            
    for ans in time:
        if(ans>=0):
            print("%.10f" % ans)
            break
    
    
    

"""
Test cases! 

5
3 0 0 -10 -10 0 0 10 0 0 -3 0 3
8 4 0 -8 -16 0 3 -4 0 -0 -6 0 5
-35 30 0 55 -20 0 -10 -10 0 9 0 0 7
-250 0 0 300 100 0 0 50 0 10 0 0 100
-10 10 0 40 0 0 -10 -10 0 0 0 0 10

"""
 