#STATUS WRONG ANSWER

#HACKERRANK WORLC CODE SPRINT


n,m,a,b,f,s,t=[int(x) for x in input().split()]


which_grade={}
for i in range(n):
    name,grade=input().split()
    which_grade[name]=int(grade)

which_group={}
groups=[]
maxims={1:f,2:s,3:t}  #grade maximums in a groups 
index=0
tracker=[] #tracks f,s,t boundaries for every group

for i in range(m):
    person1,person2=input().split()
    if(person1 in which_group and person2 not in which_group):
        group_no=which_group[person1]
        grade=which_grade[person2]
        if(len(groups[group_no])<b and tracker[group_no][grade]<maxims[grade]): #upper bound
            
            groups[group_no].append(person2)
            tracker[group_no][which_grade[person2]]+=1
            which_group[person2]=group_no
    elif(person2 in which_group and person1 not in which_group):
        group_no=which_group[person2]
        grade=which_grade[person1]
        if(len(groups[group_no])<b and tracker[group_no][grade]<maxims[grade]): #upper bound
            groups[group_no].append(person1)
            tracker[group_no][which_grade[person1]]+=1
            which_group[person1]=group_no

    elif(person1 not in which_group and person2 not in which_group):
        
        groups.append([person1,person2])
        which_group[person1]=index
        which_group[person2]=index
        tracker.append({1:0,2:0,3:0})
        tracker[index][which_grade[person1]]+=1
        tracker[index][which_grade[person2]]+=1
        index+=1
    #case where two groups need to be clubbed! into one
    
    elif(person1 in which_group and person2 in which_group):
        group_no1=which_group[person1]
        group_no2=which_group[person2]
        if(group_no1==group_no2):
            continue 
        l1=len(groups[group_no1])
        l2=len(groups[group_no2])
        if(l1+l2<=b):
            groups[group_no1]=(groups[group_no1]+groups[group_no2])
            
            for ele in groups[group_no2]:
                which_group[ele]=group_no1 #renaming the groups to which they belong 
                tracker[group_no1][which_grade[ele]]+=1
    

winners=[]
max_size=0
for g in groups:
    size=len(g)
    if(size>=a and size<=b):
        if(size>max_size):
            max_size=size
            winners=g
        elif(size==max_size):
            winners+=g
if(len(winners)==0):
    print("no groups")
else:
    winners=sorted(winners)
    for i in winners:
        print(i)