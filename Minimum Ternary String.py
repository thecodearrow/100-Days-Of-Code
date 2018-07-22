#http://codeforces.com/problemset/problem/1009/B

s=input()
count_ones=0

for c in s:
	if(c=='1'):
		count_ones+=1

s=s.replace('1','')

index=s.find('2')
if(index==-1):
	index=len(s)
ones='1'*count_ones 
new_string=s[:index]+ones+s[index:]
print(new_string)
