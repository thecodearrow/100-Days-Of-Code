#Is one array a rotation of another? 

def is_rotation(list1, list2):
    l1=len(list1)
    l2=len(list2)
    if(l1!=l2):
        return False 
    else:
        l=l1
        start1=0
        start2=-1
        ele=list1[0]
        
        for i in range(l):
            b=list2[i]
            if(b==ele):
                start2=i
                break
        if(start2==-1):
            return False
    
        for start1 in range(l):
            if(list1[start1]!=list2[start2]):
                return False 
            start2+=1
            start2=start2%l
                
            
            
    
    return True

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
