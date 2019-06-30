#https://www.codechef.com/JUNE19B/problems/KS2

def sum_digits(n):
    sum=0
    while n!=0:
        d=n%10
        sum+=d
        n=n//10
       

    return sum

t=int(input())

while t!=0:
    t-=1
    n=int(input())
    digits_sum=sum_digits(n)
    last_digit_round_int=(10-(digits_sum)%10)%10
    round_int=int(str(n)+str(last_digit_round_int))
    print(round_int)



