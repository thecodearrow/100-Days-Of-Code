#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

prices=[7,1,5,3,6,4]
profits=[0]
current_min=10**9+7
for p in prices:
	if(p<current_min):
		current_min=p 
	elif(p>current_min):
		profits.append(p-current_min)

print(max(profits))


