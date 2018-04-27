#Saving The Universe Again (partially solved!)

t=int(input())
def calculateDamage(s):
    charge=1
    damage=0
    for c in s:
        if(c=='C'):
            charge=charge*2
        if(c=='S'):
            damage=damage+charge
    return damage


        
for i in range(1,t+1):
    impossible=False
    temp=input().strip().split()
    shield=int(temp[0])
    code=temp[1]
    swaps=0
    while(calculateDamage(code)>shield):
        code_now=code.replace('CS','SC',1)
        if(code_now==code):
            impossible=True
            break
        else:
            code=code_now
            swaps=swaps+1
            
    if(impossible):
        print('Case #'+str(i)+': IMPOSSIBLE')
    else:
        print('Case #'+str(i)+':',swaps)
        
        
    
    