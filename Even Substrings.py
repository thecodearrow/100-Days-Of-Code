#https://codeforces.com/contest/1139/problem/A

l=int(input())
s=input()
count=0

for i in range(l-1,-1,-1):
    c=s[i]
    if(int(c)%2==0):
        count+=(i+1)

print(count)