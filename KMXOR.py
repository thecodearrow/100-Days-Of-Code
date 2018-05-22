#May CookOff 2018 Best Cake Ever

t=int(input())
 
while(t!=0):
    t-=1
    n,k=[int(x) for x in input().split()]
    
    count=n
    
    num1=k 
    ones='1'* len(bin(k)[2:])  #all ones  a^b=c a^c=b trying 
    ones_int= int(ones,2)
    num2=num1^ones_int #compliment
    
    #if num2==0 
    
    ones='1'* len(bin(k-1)[2:])
    ones_int= int(ones,2)
    num2_alt=(num1-1)^ones_int
   
    if(n==1):
        print(k)
        
    elif(k==1):
        while(count!=0):
            count-=1 
            print(1,end=' ')
        print('')    
    elif(n==2):
        if(num2==0):
            print(num1-1,num2_alt)
        else:
            print(num1,num2)
    
    elif(k==2):
        print(2,end=' ')
        count-=1
        while(count!=0):
            count-=1 
            print(1,end=' ')
        print('')
    elif(k==3):
        if(n%2==0):
            print(2,end=' ')
        else:
            print(3,end=' ')
        count-=1
        while(count!=0):
            count-=1 
            print(1,end=' ')
        print('')
    elif(n%2==0):
        if(num2==0):
            print(num1-1,num2_alt,end=' ' )
        else:
            print(num1,num2,end=' ')
        count-=2   
        while(count!=0):
            count-=1 
            print(1,end=' ')
        print('')
    
        
    elif(n%2!=0):
        if(num2==0):
            print(num1,end=' ')
            count-=1 
            while(count!=0):
                count-=1 
                print(1,end=' ')
            print('')
        else:
            if(num2==1):
                print(num1-1,num2_alt^1,1,end=' ')
                
            else:
                print(num1,(num2^1),1,end=' ')
                
            count-=3
            while(count!=0):
                count-=1 
                print(1,end=' ')
            print('') 