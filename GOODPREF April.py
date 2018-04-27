# cook your dish here
t=int(input())
 
for i in range(t):
    temp=input().strip().split()
    s=temp[0]
    l=len(s)
    n=int(temp[1])
    freq={'a':0,'b':0} #keeps track of a's and b's
    count=0
    i=0 #processing n bits at a time and reset i
    constancy_check=[0] #to check when to stop processing
    counts_tracker=[0]  #keeping track of counts per n bits
    index=-1
    cycles=0
    while(index<l):
        if(cycles==n):
            break
        index=index+1 
        c=s[index]
        freq[c]+=1
        if(freq['a']>freq['b']):
            count=count+1
        if(i==l-1):
            i=0 #reset
            cycles=cycles+1
            index=-1 #start over
            constancy_check.append(count-counts_tracker[-1])
            counts_tracker.append(count)
            if(constancy_check[-1]==constancy_check[-2]):
                break
        else:
            i=i+1
           
    count=count+(n-len(constancy_check)+1)*constancy_check[-1]
    print(count)   