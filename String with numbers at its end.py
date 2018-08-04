#https://practice.geeksforgeeks.org/problems/string-with-numbers-at-its-end/0

#Bad problem wording... number can be in the middle too 

t=int(input())

while t!=0:
    t-=1
    s=input()
    word=""
    numbers=set(['0','1','2','3','4','5','6','7','8','9'])
    number=""
    reverse=s[::-1]
    numFound=False
    for c in reverse:
        if(c in numbers):
            number+=(c)
            numFound=True
        elif(numFound):
            break
            
    number=number[::-1]
    given=len(s)-len(number)
    number=int(number)
    if(number==given):
        print(1)
    else:
        print(0)

