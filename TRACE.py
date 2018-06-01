# May Lunchtime 2018 Division 2  » Trace of Matrix

t=int(input())

while(t!=0):
    t-=1 
    n=int(input())
    m=[] 
    for i in range(n):
        temp=[int(x) for x in input().split()]
        m.append(temp)
        
   
    row=0 
    col=0 
    k=n  
    diagonal=[]
    sumt=0
    for i in range(k):
        sumt+=m[i][i]
        diagonal.append([i,i])
        
    traces=[sumt]
    times=k 
    while(k!=0):
        times=times-1
        index=[]
        sum_trace1=0 
        sum_trace2=0
        for i in range(times):
            row=diagonal[i][0]
            col=diagonal[i][1]+1
            sum_trace1+=m[row][col]
            sum_trace2+=m[col][row]
            diagonal[i]=[row,col]
            
        traces.append(max(sum_trace1,sum_trace2))
            
        k-=1
    print(max(traces))
        