#Chef Restores a Matrix Problem Code: CO92MATR

"""

Chef defines a non-decreasing matrix as a matrix that satisfies the following rules:

For each row of the matrix, the elements of this row form a non-decreasing sequence.
For each column of the matrix, the elements of this column form a non-decreasing sequence.
Chef has a matrix A with size N × M. Each element of this matrix is either unknown (denoted by -1) or a positive integer.

Chef would like to replace each unknown element of this matrix by a positive integer in such a way that the resulting matrix is non-decreasing. Find one possible resulting matrix or determine that it's impossible.


"""

t=int(input())
 
def findFit(left,top):
    return(max(left,top))
    
 
while(t!=0):
    t=t-1
    n,m=[int(x) for x in input().strip().split()]
    matrix = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        matrix[i]=[int(x) for x in input().strip().split()]
    
    
    impossible=False
    for i in range(n):
        for j in range(m):
                if(i==0 and j==0):
                    if(matrix[i][j]==-1):
                        matrix[i][j]=1 #extreme
                elif(i==0):
                    
                    if(matrix[i][j]==-1):
                        matrix[i][j]=matrix[i][j-1]
                elif(j==0):
                    
                    if(matrix[i][j]==-1):
                        matrix[i][j]=matrix[i-1][j]
                else: #regular case
                    
                    if(matrix[i][j]==-1):    
                        matrix[i][j]=findFit(matrix[i][j-1],matrix[i-1][j])
    
    for i in range(n):
        for j in range(m):
            if(i==0 and j==0):
                pass
            elif(i==0):
                if(matrix[i][j]<matrix[i][j-1]):
                        impossible=True
                        break
            elif(j==0):
                if(matrix[i][j]<matrix[i-1][j]):
                        impossible=True
                        break
            else:
                if(matrix[i][j]<matrix[i][j-1] or matrix[i][j]<matrix[i-1][j]):
                        impossible=True
                        break
    
                
    if(impossible==False):
        for i in range(n):
            for j in range(m):
                print(matrix[i][j],end=' ')
            print()
    else:
        print(-1)