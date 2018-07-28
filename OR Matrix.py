#July Cook-Off 2018 Division 2

#https://www.codechef.com/COOK96B/problems/ORMATRIX

t=int(input())
while t!=0:
    t-=1
    n,m=[int(x) for x in input().split()]
    ans={}
    matrix=[]
    for i in range(n):
        s=input()
        row=list(s)
        row=[int(x) for x in s]
        matrix.append(row)
 
    impossible=True
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==1):
                impossible=False
                break
 
 
    if(impossible):
        for i in range(n):
            for j in range(m):
                print(-1,end=' ')
            print()
    else:
        lucky_row=set()
        lucky_col=set()
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==1):
                    lucky_row.add(i)
                    lucky_col.add(j)
 
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==1):
                    ans[i,j]=0
                elif(i in lucky_row or j in lucky_col):
                    ans[i,j]=1 
                else:
                    ans[i,j]=2
 
 
        for i in range(n):
            for j in range(m):
                print(ans[i,j],end=' ')
            print()