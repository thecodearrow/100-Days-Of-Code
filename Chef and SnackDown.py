#https://www.codechef.com/SNCK1B19/problems/SNCKYEAR

snackdown=set([2010, 2015, 2016, 2017,2019])

t=int(input())

while t!=0:
    t-=1
    n=int(input())
    if(n in snackdown):
        print("HOSTED")
    else:
        print("NOT HOSTED")
