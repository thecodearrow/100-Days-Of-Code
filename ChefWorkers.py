# Workers Problem Code: CHEFWORK

n=int(input())
coins=[int(x) for x in input().strip().split()]
types=[int(x) for x in input().strip().split()]

if(1 not in types and 2 not in types ):
    print(min(coins))
else:
    ulti_1=[]
    ulti_2=[]
    ulti_3=[]
    for i in range(n):
        if(types[i]==1):
            ulti_1.append(coins[i])
        elif(types[i]==2):
            ulti_2.append(coins[i])
        elif(types[i]==3):
            ulti_3.append(coins[i])
    
    ulti_1=sorted(ulti_1)
    ulti_2=sorted(ulti_2)
    ulti_3=sorted(ulti_3)
    alt=-1
    minimum=-1
    if(ulti_3):
        minimum=ulti_3[0]
    if(ulti_1 and ulti_2):
        alt=ulti_1[0]+ulti_2[0]
        
    if(minimum!=-1 and alt!=-1 and minimum<alt):
        print(minimum)
    elif(alt==-1):
        print(minimum)
    else:
        print(alt)
        
        