
from collections import Counter
def isValidPalindrome(s):
	cnt=Counter(s)
	odd_freq=0
	for c in cnt:
		if(cnt[c]%2!=0):
			odd_freq+=1
			if(odd_freq>1):
				return False
	return True
#https://www.codechef.com/problems/ENCD12

while True:
	s=input().strip()
	if(s=='0'):
		break
	s=list(s)
	if(isValidPalindrome(s)):
		l=0
		r=len(s)-1
		swaps=0
		while l<r:
			left_char=s[l]
			right_char=s[r]
			if(left_char==right_char):
				l+=1
				r-=1
			else:
				i=r
				#try to find left char moving from right! 
				while i>l and s[i]!=left_char:
					i-=1
				if(i==l):
					#no match, try to move it towards center! 
					s[i],s[i+1]=s[i+1],s[i]
					swaps+=1
				else:
					for curr_i in range(i,r):
						s[curr_i],s[curr_i+1]=s[curr_i+1],s[curr_i]
						swaps+=1
					l+=1
					r-=1
		print(swaps)
	else:
		print("Impossible")
