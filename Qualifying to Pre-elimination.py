#https://www.codechef.com/SNCKQL19/problems/QUALPREL

#reference https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-3-worst-case-linear-time/

#https://stackoverflow.com/questions/10806303/python-implementation-of-median-of-medians-algorithm

def qSelect(A, i):
    t = len(A)

    if(t <= 15):
       	val=sorted(A)[i]
        return val
    else:
       
        B = [ qSelect(k, (len(k) - 1)/2) for k in [A[j:(j +15)] for j in range(0,len(A),15)]]

      
        M = qSelect(B, (len(B) - 1)/2)

        
        P1 = [ j for j in A if j < M ]
        if(i < len(P1)):
            return qSelect( P1, i)
        P3 = [ j for j in A if j > M ]
        L3 = len(P3)
        if(i < (t - L3)):
            return M
        return qSelect( P3, i - (t - L3))



t=int(raw_input())
while t!=0:
    t-=1
    n,k=[int(x) for x in raw_input().split()]
    array=[int(x) for x in raw_input().split()]
    number=qSelect(array,n-k)
    count=0
    for a in array:
        if(a>=number):
            count+=1
    print(count)

