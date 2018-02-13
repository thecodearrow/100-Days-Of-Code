"""

You are given an array A[N] of size N.
We define a 7-Divisible Pair as a pair of integers (i,j) such that Ai + Aj is divisible by 7.
Formally, a pair of integers (i,j) is a 7-Divisible pair if ( Ai + Aj ) % 7 = 0.
Your task is to find the total number of 7-Divisible pairs from the given array.

INPUT

First line contains N the size of the array. (1 ≤ N ≤ 105).
Second line contains the array elements that all lie between 1 and 105.

OUTPUT

Output a single integer that denotes the number of pairs divisible by 7.

Sample Input 0

5
9 3 7 4 14

Sample Output 0

2

"""

n=int(input())
l=[int(i) for i in input().split()]

modulo={0:0,1:0,2:0,3:0,4:0,5:0,6:0}

for num in l:
    remainder=num%7
    modulo[remainder]=modulo[remainder]+1

    
    count=modulo[0]*(modulo[0]-1)/2 #nC2
    count=count+modulo[1]*modulo[6]
    count=count+modulo[2]*modulo[5]
    count=count+modulo[3]*modulo[4]
print(int(count))
    