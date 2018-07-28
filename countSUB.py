"""
Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
In this problem, a substring is defined as a sequence of continuous characters Si, Si+1, ..., Sj where 1 ≤ i ≤ j ≤ N
"""

def startsEndsWith(s):
    if(s.startswith('1') and s.endswith('1')):
        return True
    else:
        return False
        
T=int(input())
for i in range(T):
    l=int(input())
    string=input()
    substrings=[string[i:j] for i in range(l) for j in range(i+1,l+1)] 
    count=0
    for sub in substrings:
        if(startsEndsWith(sub)):
            count=count+1
    print(count)