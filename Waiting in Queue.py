#https://www.codechef.com/SNCK1B19/problems/QUEUE2


t=int(input())

while t!=0:
    t-=1
    n,m,k,l=[int(x) for x in input().split()]
    queue=[int(x) for x in input().split()]
    queue=sorted(queue)  #sorting based on wait times!
    first_slot=(m+1)*l 
    last_slot=(m+n+1)*l  #after everyone in the queue is served!

    best=[] #waiting times

    if first_slot<=queue[0]:
        print(0) #first slot is free even before first person in queue arrives

    elif last_slot<=k:
        print(0) #arrive whenever you want since there's no queue now


    else:
        
        free_slots=[]
        for i in range(1,n+1):
            free_slots.append(l*(m+i))


        queue=sorted(queue)[::-1]  

        #remove all wait times > k 
        new_queue=[]
        for q in queue:
            if(q<=k):
                new_queue.append(q)


        waiting_times=[last_slot-k]   #after the last person but before k!
        for f in free_slots:
            if(queue):
                time=queue.pop()
                if(f<=time):
                    #come exactly at that time before the next person
                    waiting_times.append(0)
                else:
                    waiting_times.append(f-time) #exactly enough to beat the current guy


        print(min(waiting_times))







