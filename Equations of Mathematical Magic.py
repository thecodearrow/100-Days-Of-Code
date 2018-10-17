#http://codeforces.com/contest/1064/problem/B

t=int(input())
while t!=0:
    t-=1
    n=int(input())
    b=bin(n)[2:]
    count=0
    for c in b:
        if c=='1':
            count+=1

    print(2**count)