#Codeforces 999B Reversing Encryption

n,k=[int(x) for x in input().split()]

s=input()
s=list(s)
delete=[]
for j in range(k):
    for ascii in range(97,123):
        elem=chr(ascii)
        i= s.index(elem) if elem in s else -1
        if(i!=-1):
            del(s[i])
            break
        
print(''.join(s))
 
            


