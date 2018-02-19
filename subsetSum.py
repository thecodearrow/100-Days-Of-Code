

arr=[1,2,3,4,5,6]
count=len(arr)
memo={}


def countSubsets(sum,index):
    key=str(sum)+"@"+str(index)
    if(key in memo):
        return memo[key]
    
    if(sum==0):
        return 1
    if(sum<0 or index<0):
        return 0
    
    if(sum<arr[index]):
        to_return=countSubsets(sum,index-1)
    else:
        to_return=countSubsets(sum,index-1)+countSubsets(sum-arr[index],index-1)
    memo[key]=to_return
    return to_return

countSubsets(11,count-1)
print(memo["11@5"])
