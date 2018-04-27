

 
"""VK gave a problem to Chef, but Chef is too lazy, so he asked you to solve the problem for him. The statement of the problem follows.

Consider an integer with NN digits (in decimal notation, without leading zeroes) D1,D2,D3,…,DND1,D2,D3,…,DN. Here, D1D1 is the most significant digit and DNDN the least significant. The weight of this integer is defined as
∑i=2N(Di−Di−1).
∑i=2N(Di−Di−1).
You are given integers NN and WW. Find the number of positive integers with NN digits (without leading zeroes) and weight equal to WW. Compute this number modulo 109+7109+7."""
 
#(A * B) mod C = (A mod C * B mod C) mod C
 
#w=last-first
 
#no.of last, first combos * 10*n-2 = ans

t=int(input())
for i in range(t):
    n,w=[int(x) for x in input().strip().split()]
    F=1
    if(w<0):
        F=0 #last digit can be zero!
    count=0
    while(F+abs(w)<10):
        count=count+1
        F=F+1
    modulo=10**9+7
    A=count
    C=modulo
    middle_irrelevant_combos=pow(10,n-2,modulo) #taking modulo since it is large
    B_modC=middle_irrelevant_combos
    ans=(A%C * B_modC)%C
    print(ans)