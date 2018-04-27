t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    freq={}
    unique_arr=[]
    for ele in arr:
        if(ele not in freq):
            unique_arr.append(ele)
            freq[ele]=1
        else:
            freq[ele]+=1
    count=0
    length=len(unique_arr)
    for i in range(length):
        pair1=unique_arr[i]
        if(freq[pair1]>1):
            count=count+(freq[pair1]*(freq[pair1]-1))/2
        for j in range(i+1,length):
            pair2=unique_arr[j]
            if(pair1!=pair2 and (pair1+pair2)%2==0):
                avg=(pair1+pair2)/2 #checck for pair2 presence!
                if(avg in freq):
                    count=count+freq[pair1]*freq[pair2]
        
    print(int(count))    
