#http://codeforces.com/contest/1064/problem/A

tri=[int(x) for x in input().split()]

tri=sorted(tri)
a,b,c=tri[0],tri[1],tri[2]
s=a+b
if(s>c):
    print(0)
else:
    print((c+1)-(b+a))