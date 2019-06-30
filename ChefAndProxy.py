#https://www.codechef.com/JUNE19B/problems/PROXYC
import math
t=int(input())

while t!=0:
    t-=1
    days=int(input())
    attendance=input()
    days_present=0
    for d in attendance:
        if(d=="P"):
            days_present+=1
    required_proxies=math.ceil(0.75*days)-days_present

    if(required_proxies<0):
        required_proxies=0 #edge case when proxies aren't required

    proxies_posssible=0
    for i in range(2,days-2):
        if(attendance[i]=="A"):
            if((attendance[i-1]=="P" or attendance[i-2]=="P") and (attendance[i+1]=="P" or attendance[i+2]=="P")):
                proxies_posssible+=1

    if(proxies_posssible>=required_proxies):
        print(required_proxies)
    else:
        print(-1)


