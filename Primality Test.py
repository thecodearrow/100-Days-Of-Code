t=int(input())
while(t!=0):
    t=t-1
    #Fermat's theorem for primality
    #Remember Carmichael numbers fail this test
    n=int(input())
    a=2  #test for a=3,4,5....n 
    ferm=a**n-a 
    if(ferm%n==0):
        print("yes")
    else:
        print("no")







#OR


n=int(input())

small_primes=[2,3,5,7,11,13,17,23,29,31,37]
if(n in small_primes):
    print("PRIME")
elif(pow(2,n-1,n)==1): #561 is composite but goes through!
    composite=False
    for i in small_primes:
        if(n%i==0):
            print("COMPOSITE")
            composite=True
            break
        
    if(not composite):
        print("PRIME")
    
else:
    print("COMPOSITE")