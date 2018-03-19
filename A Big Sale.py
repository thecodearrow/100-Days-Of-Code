#March Challenge 2018 DIV 2

t=int(input())

while(t!=0):
    t=t-1
    n=int(input())
    losses=[]
    for i in range(n):
        receipe=[int(x) for x in input().strip().split()]
        price=receipe[0]
        quantity=receipe[1]
        discount=receipe[2]
        amt=price+price*(discount/100)
        amt=amt-amt*(discount/100)
        loss=(price-amt)*quantity
        losses.append(loss)
    print("%.10f"% sum(losses))
    
        
        